from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.contrib.auth import get_user_model, get_user
from .forms import PostForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user = get_user(request)
        posts = Post.objects.filter(author=user)
        return render(request, 'home.html', {'posts': posts})
    else:
        return render(request, 'home.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})