from django import forms
from  django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserAccount,publisherInfo

#This form is crearted for the resgistion  
class RegistationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        our_user = super().save(commit=False)
        our_user.first_name = self.cleaned_data['first_name']
        our_user.last_name = self.cleaned_data['last_name']
        our_user.email = self.cleaned_data['email']

        if commit:
            our_user.save()
            if not hasattr(our_user, 'account'):
                UserAccount.objects.create(user=our_user)
        return our_user


class ChangeUserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class PublisherRegister(forms.ModelForm):
    class Meta:
        model = publisherInfo
        fields = ['image','spaciality','about']