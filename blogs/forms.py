from django import forms

from .models import BlogPost
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'image','owner']
        labels = {'title': 'Title', 'text': 'My text'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        



