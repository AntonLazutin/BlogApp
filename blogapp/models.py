from statistics import mode
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
    #likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name="post_liked")
    dislikes = models.IntegerField(default=0)
    
    class Meta:
        db_table = "post"
        ordering = ['-date']

    def __str__(self):
        return self.title[:10] + '...'

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.id})
    

    def get_total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(default="Anon", max_length=100) 
    text = models.CharField(max_length=100, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "comment"
        ordering = ['date_added']

    def __str__(self):
        return self.text