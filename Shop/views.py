from django.shortcuts import render
from django.http import HttpResponse
from Shop.models import Product
from math import ceil

# Create your views here.

def index(request):
    # products = Product.objects.all()
#    params = {"no_of_sldes":nslides , "range" : range(1,nslides) ,"products" : products}
    # allProds = [[products,range(1,nslides),nslides],
    # [products,range(1,nslides),nslides]]
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)+(n//4))
        allProds.append([prod,range(1,nslides),nslides]) 

    params = {"allProds":allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/aboutUs.html')

def contact(request):
    return render(request,'shop/contactUs.html')

def tracker(request):
    return render(request,'shop/trackingOrder.html')

def search(request):
    return render(request,'shop/search.html')

def productView(request):
    return render(request,'shop/productView.html')

def checkout(request):
    return render(request,'shop/checkout.html')