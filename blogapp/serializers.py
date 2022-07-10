from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Post
        fields = ('title', 'text', 'author', 'date', 'id')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)
