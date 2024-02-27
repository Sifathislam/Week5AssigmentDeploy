from django import forms
from .models import review, Book


class reviewForm(forms.ModelForm):
    class Meta: 
        model = review
        fields = ['name', 'body']

class Add_Books(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['image','title','category','price', 'quntity','description']