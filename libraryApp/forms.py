from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserRegisterForm(UserCreationForm):
   email = forms.EmailField(max_length=200, help_text = 'Required')
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ['book_id']
