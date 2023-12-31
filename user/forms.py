from django import forms
from  django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserAccount

#This form is crearted for the resgistion  
class RegistationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
    def save(self, commit=True):
            our_user = super().save(commit=False) # ami database e data save korbo na ekhn
            if commit == True:
                our_user.save() # user model e data save korlam
                UserAccount.objects.create(
                    user = our_user,)
            return our_user


class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']