from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from trasactions.forms import DepositForm
from trasactions.models import Transaction
from user.models import UserAccount
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    success_url = reverse_lazy('homepage')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account  # Assuming UserAccount is associated with the user model
        })
        return kwargs


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account  # Assuming UserAccount is associated with the user model

        # Create a Transaction instance
        transaction = form.save(commit=False)
        transaction.account = account
        transaction.save()

        # Update the user's balance
        account.balance += amount
        account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )
        send_transaction_email(self.request.user, amount, "Deposite Message", "depsosite_email.html")

        return super().form_valid(form)
