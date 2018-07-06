from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from products.models import Product
from .utils import get_cart_items_and_total
# Create your views here.

def view_shortlist(request):
    shortlist = request.session.get("shortlist", {})
    context = get_cart_items_and_total(shortlist)
        
    return render(request, "shortlist/viewshortlist.html", context)

def add_to_shortlist(request):
    id = request.POST["product_id"]
    product = get_object_or_404(Product, pk=id)
    shortlist = request.session.get("shortlist", {})
    shortlist[id] = shortlist.get(id, 0) + 1
    request.session["shortlist"] = shortlist
    return redirect("get_products")   
    
def remove_from_shortlist(request):
    id = request.POST["product_id"]
    product = get_object_or_404(Product, pk=id)
    shortlist = request.session.get("shortlist", {})
    if shortlist[id] > 1:
        shortlist[id] = shortlist.get(id, 0) - 1
    else:
        del shortlist[id]
    request.session["shortlist"] = shortlist
    return redirect("view_shortlist")
