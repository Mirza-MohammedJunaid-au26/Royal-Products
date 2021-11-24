from django.shortcuts import render
from django.http import HttpResponse
from Shop.models import Product
from math import ceil

# Create your views here.

def index(request):
    products = Product.objects.all()
    n = len(products)
    nslides = n//4 + ceil((n/4)+(n//4))
#    params = {"no_of_sldes":nslides , "range" : range(1,nslides) ,"products" : products}
    allProds = [[products,range(1,nslides),nslides],
    [products,range(1,nslides),nslides]]
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