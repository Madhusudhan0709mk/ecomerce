from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'index.html',context)

def cart(request):
    return render(request,'cart/cart.html')

def product(request,id):
    product_view = Product.objects.get(id=id)
    context={
        'product_view':product_view
    }
    return render(request,'product/product.html',context)