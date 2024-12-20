from django import forms
from .models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')