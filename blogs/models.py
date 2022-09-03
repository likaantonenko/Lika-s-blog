from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    text = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete=, blank=True, null=True
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost,  related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


