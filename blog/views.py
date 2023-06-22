from django.shortcuts import render, redirect, get_object_or_404
from account.models import Profile
from .models import Post, Comment
from django.contrib import messages

# Create your views here.


def home_post(request):
    if not request.user.is_authenticated:
        post = Post.objects.all()
        return render(request, 'blog/index.html', {'posts': post})
    else:
        profile = Profile.objects.get(user=request.user)
        post = Post.objects.all()
        return render(request, 'blog/index.html', {'profile': profile, 'posts': post})


def detail_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'blog/detail_page.html', {'post': post})


def post_comment(request, pk):
    post = Post.objects.filter(id=pk).first()
    Comment.objects.create(body=request.POST.get('comment'), post=post, user=request.user)
    redirect_url = request.META.get('HTTP_REFERER')
    return redirect(redirect_url)


def edit_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.body = request.POST.get('comment')
    comment.save()
    messages.warning(request, 'Comment successfully edited')
    redirect_url = request.META.get('HTTP_REFERER')
    return redirect(redirect_url)


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    messages.warning(request, 'Comment successfully deleted')
    redirect_url = request.META.get('HTTP_REFERER')
    return redirect(redirect_url)
