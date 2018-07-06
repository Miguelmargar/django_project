from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(shortlist):    
    shortlist_total = 0
    shortlist_items = []
    for p in shortlist:
        product = get_object_or_404(Product, pk=p)
        quantity = shortlist[p]
        
        shortlist_item = {
          "product": product,
          "quantity": quantity,
          "sub_total": product.price * quantity
        }
        shortlist_items.append(shortlist_item)
        shortlist_total += shortlist_item["sub_total"]

    return {"shortlist": shortlist_items, "shortlist_total": shortlist_total }