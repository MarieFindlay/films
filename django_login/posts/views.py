from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})