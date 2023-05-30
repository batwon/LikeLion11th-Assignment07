from django.shortcuts import render
from .models import Blogs

# Create your views here.

def jiwon(request):
    blogs = Blogs.objects.all
    return render(request, 'jiwon.html', {'blogs': blogs})

def main(request):
    blogs = Blogs.objects.all
    return render(request, 'main.html', {'blogs': blogs})
