from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('id', 'author')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)


class SignUpForm(forms.Form):
    form = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = "signup.html"
