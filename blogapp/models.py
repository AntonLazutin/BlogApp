from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.utils.timezone import now
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=30, null=False)
    text = models.CharField(max_length=300, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(default=now, editable=False)
    id = models.BigAutoField(primary_key=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:10] + '...'

    def get_absolute_url(self):
        return reverse('posts/', kwargs={'slug': self.title.replace(' ', '_')})

    def liked(self):
        self.likes += 1
        self.save()

    def disliked(self):
        self.dislikes += 1
        self.save()


class UserProfile(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    posts_list = models.ForeignKey(Post, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.account.username


class Comment(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
