from django.shortcuts import render
from .models import Product
from django.db.models import Q
# Create your views here.

def get_products(request):
    query = request.GET.get("search", "")
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(collection__icontains=query))
    return render(request, "products/products.html", {"products": products})
    
