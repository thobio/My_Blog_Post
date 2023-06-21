from django.shortcuts import render
from account.models import Profile
from .models import Post

# Create your views here.


def home_post(request):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.all()
    return render(request, 'blog/index.html', {'profile': profile, 'posts': post})
