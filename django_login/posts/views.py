from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth import get_user_model, get_user

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user = get_user(request)
        posts = Post.objects.filter(author=user)
        return render(request, 'home.html', {'posts': posts})
    else:
        return render(request, 'home.html', {})