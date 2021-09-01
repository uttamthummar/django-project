
from django.shortcuts import get_object_or_404, redirect, render
from .models import *

def dashboard(request):
    return render(request,"dashboard.html")

def home(request):
    return render(request,"main.html")

def shop(request):
    clothes = Clothes.objects.all()
    return render(request,"shop.html",{'clothes':clothes})
    
def product_add(request):
    if request.method == "POST":
        if (request.POST.get("product_name") and request.POST.get("product_price")) or request.POST.get("description"):
            product=Product()
            product.product_name=request.POST.get("product_name")
            product.product_price=request.POST.get("product_price") 
            product.description=request.POST.get("description")
            product.save()
            product = Product.objects.all()
            return redirect(list)
        else:
            return redirect(product_add)
    else:
        return render(request,"form.html")

def product_delete(request,id):
    product=Product.objects.get(id=id).delete()
    return redirect(list)


def list(request):
    product=Product
    product = Product.objects.all()
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
