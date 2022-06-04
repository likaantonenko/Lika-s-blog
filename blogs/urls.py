from django.urls import path
from . import views
import blogs


app_name = 'blogs'
urlpatterns = [
    #main page
    path('', views.index, name='index'),
    #сторінка з постиками
    path('posts/', views.posts, name='posts'),
    #сторінка окремого посту
    path('post/<int:post_id>/', views.post, name='post'),
    #сторінка для додавання нового посту
    path('new_post/', views.new_post, name='new_post'),
    #сторінка для редагування посту
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
   
]
