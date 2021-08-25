from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *

def dashboard(request):
    return render(request,"dashboard.html")

def home(request):
    return render(request,"main.html")

def shop(request):
    return render(request,"shop.html")

def features(request):
    return render(request,"features.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")

def Contact(request):
    return render(request,"Contact.html")
    
def search(request):
    return render(request,"searchbar.html")