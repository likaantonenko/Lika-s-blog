from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import PostForm

def index(request):
    return render(request, 'blogs/index.html')

def posts(request):
    #show all posts
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    #show a single post
    post = BlogPost.objects.get(id=post_id)
    title = post.title
    text = post.text
    context = {'post': post, 'title': title, 'text': text}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    #add new post
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('blogs:posts')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

