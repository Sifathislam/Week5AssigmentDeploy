from django.shortcuts import render,redirect
from . import forms
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from books.models import Purcehase_history
# This Class based user registation form 
class SignUpViewClass(SuccessMessageMixin, CreateView):
     template_name = 'form.html'
     success_url = reverse_lazy('register')
     form_class = forms.RegistationForm
     success_message = "Your account was created successfully "

     def form_valid(self,form):
          response = super().form_valid(form)
          messages.success(self.request, self.success_message)
          return response
     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['type'] = 'Register'
         return context

# This Class based user Login  

class UserLoginViewClass(LoginView):
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'You are successfully logged in')
        # form
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Your provided information is incorrect')
        # form
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

# This Class based user Logout
@method_decorator(login_required, name= 'dispatch')
class UserLogoutViewClass(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
       return reverse_lazy('homepage')
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        messages.success(self.request, "You have been successfully logged out.")
        return response
    
@method_decorator(login_required, name= 'dispatch')
class ProfileView(View):
    template_name = 'profile.html'
    def get(self, request, *agrs, **kwargs):
        data = Purcehase_history.objects.filter(user=request.user)
        return render(request, 'profile.html',{'data':data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})


@method_decorator(login_required, name= 'dispatch')
class ChangePassWordClass(PasswordChangeView):
    template_name = 'changepassword.html'
    success_url = reverse_lazy('profile')
    success_message = "Your Password Successfully Changed"
    def form_valid(self,form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response