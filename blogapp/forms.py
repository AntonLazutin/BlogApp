from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('id', 'author', 'likes', 'dislikes')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20  , required=True)


class SignUpForm(forms.Form):
    form = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = "signup.html"


class CommentForm(forms.Form):
    class Meta:
        model = Comment
        exclude = ('post', 'date_added')