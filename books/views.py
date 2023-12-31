from django.shortcuts import render,redirect
from . import models
from books.models import Book
from books.models import review,Purcehase_history
from books.forms import reviewForm
from user.models import UserAccount
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives


# Create your views here.
def send_transaction_email(user, subject, template):
        message = render_to_string(template, {
            'user' : user,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

def ViewDetails(request, id):
    book = Book.objects.get(pk=id)
    comments = review.objects.all()

    if request.method == 'POST':
        comment_form = reviewForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = book
            comment.save()
    else:
        comment_form = reviewForm()
    if request.user.is_authenticated:
        is_borrowed = Purcehase_history.objects.filter(user=request.user, Book=book, isBorrowd=True).exists()
        return render(request, 'view_details.html', {'object': book, 'comment_form': comment_form, 'comment': comments, 'isBorrowed': is_borrowed})
    else:
        return render(request, 'view_details.html', {'object': book})


def borrow(request, id, userid):
    userid-=1
    print(userid)
    data = Book.objects.get(pk=id)
    account = UserAccount.objects.get(pk=userid)  # Assuming there's a specific account you want to use for testing
    quntity = data.quntity
    price = data.price
    balance = account.balance
    purchase_history=False

    if balance > price and quntity > 1:
        quntity -= 1
        balance -= price
        account.balance = balance

        data.quntity = quntity
        data.save()

        # Assuming you have a ForeignKey from Purcehase_history to Book called 'Book'
        purchase_history = Purcehase_history.objects.create(user=request.user, Book=data)
        account.save()

        messages.success(
            request,
            f'You have successfully borrowed a book'
        )

        send_transaction_email(request.user, "Book Borrwed Message", "bookBorwwed.html")
        return redirect('profile')
    else:
        messages.warning(
            request,
            f'Your balance is not enough to buy this book or the book is finished'
        )
        send_transaction_email(request.user, "Book Borrwed Message Faild", "bookbowedfaild.html")

    return render(request, 'view_details.html', {'object': data, 'isBorrwod': purchase_history})



def bookReturn(request, id,userid,buyid):
    print(userid)
    data = models.Book.objects.get(pk=id)
    account = UserAccount.objects.get(pk=1)
    quntity = data.quntity
    price = data.price
    balance = account.balance
    if balance > price:
        if quntity > 1:
            quntity +=1
            balance+=price
            account.balance = balance
            data.quntity = quntity
            account.save()
            data.save()
            deleteHistory = models.Purcehase_history.objects.get(id = buyid)
            deleteHistory.delete()
            send_transaction_email(request.user, "Book Return Message succefully", "bookreturn.html")
            return redirect('profile')
    else:
        messages.warning(
            request,
            f'Your balance is not enough to buy this book or the book is finished'
        )
        send_transaction_email(request.user, "Book Return Message Faild", "bookreturnfaild.html")
    return render(request,'ViewDetaisl.html', {'object': data})