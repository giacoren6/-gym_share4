from django.db import models
from posts.models import Post
from profiles.models import Profile

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content[:20]