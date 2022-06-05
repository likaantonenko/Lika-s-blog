import django
from django.urls import URLPattern, path, include

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]