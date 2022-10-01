from .models import Post

def get_posts_by_user(user):
    try:
        post_queryset = Post.objects.filter(author=user)
    except Post.DoesNotExist:
        post_queryset = None
    return post_queryset


def react_to_post(user, action, pk):
    post = Post.objects.get(id=pk)
    if action == "like":
        post.liked()    
    elif action == "dislike":
        post.disliked()