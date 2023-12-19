from django import forms
from .models import *
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, SetPasswordForm, UsernameField, PasswordChangeForm, PasswordResetForm)
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError



from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(label='Enter Username', help_text='* Username should not have any space' , min_length=4, max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django.contrib.auth.forms import AuthenticationForm
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User  # You should import the User model from your authentication system
        fields = ('username', 'password')



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
        # fields = ['title', 'discription', 'image' ]
        # labels = {'title':'title', 'discription':'discription', 'image':'image' }

class PostForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput (attrs={'placeholder':"Title"}))
    description=forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter you description"}))
    image=forms.ImageField()

    
