from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request,
                  'abcd.html',
                  {'blogs' : blogs})

def post1(request):
    return render(request,
                  'post1.html')

def post2(request):
    return render(request,
                  'post2.html')