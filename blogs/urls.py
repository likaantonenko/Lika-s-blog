from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


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
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 