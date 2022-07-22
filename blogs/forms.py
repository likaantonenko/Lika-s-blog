from django import forms

from .models import BlogPost

class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'owner']
        labels = {'title': 'Zagolovok', 'text': 'My text'}

