from django import views
from django.urls import path
from .views import render_post, posts_detail

app_name = 'blog'

urlpatterns = [
    path('', render_post, name='posts'),
    path('<int:post_id>', posts_detail,name='posts_detail')
]