from turtle import title
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
