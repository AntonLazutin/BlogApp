from unicodedata import name
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User
from .models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        author = UserSerializer()
        model = Post
        fields = ('title', 'text', 'author', 'date', 'id', 'likes', 'dislikes')

