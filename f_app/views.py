from django.contrib import messages
from start_up.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect, render
from .models import *


def dashboard(request):
    return render(request,"dashboard.html")

def home(request):
    return render(request,"main.html")

def shop(request):
    clothes = Clothes.objects.all()
    return render(request,"shop.html",{'clothes':clothes})

@login_required(login_url=LOGIN_REDIRECT_URL)
def product_add(request):
    if request.method == "POST":  
        if (request.POST.get("product_name") and request.POST.get("product_price")) or request.POST.get("description"):     
            product=Product()
            product.product_name=request.POST.get("product_name")
            product.product_price=request.POST.get("product_price")
            product.description=request.POST.get("description") 
            product.name=request.user
            product.save()
            return redirect(list)
        else:
            messages.error(request,"error")
            return redirect(product_add)
    else:
        return render(request,"form.html")

@login_required(login_url=LOGIN_REDIRECT_URL)
def product_extend(request,id):
    product=Product.objects.get(id=id)
    return render(request,"extend.html",{"product":product})

@login_required(login_url=LOGIN_REDIRECT_URL)
def product_delete(request,id):
    product=Product.objects.get(id=id).delete()
    return redirect(list)

@login_required(login_url=LOGIN_REDIRECT_URL)
def product_edit(request,id):
    product=Product.objects.get(id=id)
    if request.method =="POST":
        product.product_name=request.POST.get("product_name")
        product.product_price=request.POST.get("product_price") 
        product.description=request.POST.get("description")
        product.save()
        return redirect(list)
    return render(request,"product_edit.html",{"product":product})

@login_required(login_url=LOGIN_REDIRECT_URL)
def list(request):
    product=Product()
    product.name=request.user
    product = Product.objects.filter(name=product.name).order_by("id")
    return render(request,"list.html",{"product":product})

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
