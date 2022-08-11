from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost, Comment
from .forms import PostForm, CommentForm

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
    image = post.image

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'post': post, 'title': title, 'text': text, 'image': image, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blogs/post.html', context)

'Traceback (most recent call last):\n  File "c:\\Users\\Прохор\\.vscode\\extensions\\ms-python.python-2022.12.0\\pythonFiles\\lib\\python\\debugpy\\_vendored\\pydevd\\_pydevd_bundle\\pydevd_resolver.py", line 192, in _get_py_dictionary\n    attr = getattr(var, name)\n  File "e:\\програмування\\Django_Blog\\ll_env\\lib\\site-packages\\django\\core\\files\\utils.py", line 47, in <lambda>\n    tell = property(lambda self: self.file.tell)\n  File "e:\\програмування\\Django_Blog\\ll_env\\lib\\site-packages\\django\\db\\models\\fields\\files.py", line 45, in _get_file\n    self._require_file()\n  File "e:\\програмування\\Django_Blog\\ll_env\\lib\\site-packages\\django\\db\\models\\fields\\files.py", line 40, in _require_file\n    raise ValueError(\nValueError: The \'image\' attribute has no file associated with it.\n'

@login_required
def new_post(request):
    #add new post
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid:
            # cuurent user as owner
            form.save()
            return redirect('blogs:posts')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    #пересвідчитись, що тема належить поточному користувачеві
    if post.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

# def comments(request,post_id):
#     post = BlogPost.objects.get(id=post_id)
#     # List of active comments for this post
#     comments = post.comments.filter(active=True)

#     if request.method == 'POST':
#         # A comment was posted
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     p = comment_form.as_p()

#     return render(request,
#                   'blog/post.html',
#                  {'post': post,
#                   'comments': comments,
#                   'comment_form': comment_form})


