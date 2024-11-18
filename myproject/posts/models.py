from django.db import models
from profiles.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title