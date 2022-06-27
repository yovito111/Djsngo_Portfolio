from django.shortcuts import render, get_object_or_404
from .models import Post

def render_post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def posts_detail(request, post_id):
    posts = get_object_or_404(Post, pk= post_id)
    return render(request, 'posts_detail.html', {'posts' : posts})