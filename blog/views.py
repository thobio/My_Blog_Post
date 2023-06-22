from django.shortcuts import render, redirect
from account.models import Profile
from .models import Post

# Create your views here.


def home_post(request):
    if not request.user.is_authenticated:
        post = Post.objects.all()
        return render(request, 'blog/index.html', {'posts': post})
    else:
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.all()
        return render(request, 'blog/index.html', {'profile': profile, 'posts': post})
