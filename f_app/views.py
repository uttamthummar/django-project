from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
@login_required
def user(request):
    return render(request,'user.html')

def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('user')
    else:
        form = UserCreationForm()

    return render(request,"registration/register.html",{'form':form})
def home(request):
    return render(request,"dashboard.html")

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