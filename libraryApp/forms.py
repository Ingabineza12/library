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
        exclude = ['book_id','name','author','image']

class IssueForm(forms.ModelForm):
    borrower_name = forms.CharField(
         required=False,
     )
    book_name = forms.CharField(
         required=False,
     )
    class Meta:
        model = Issue
        exclude = ['issue_date', 'book_id']

class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        exclude = ['return_date', 'book_id', 'borrower_name', 'book_name']
