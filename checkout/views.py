from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderForm, MakePaymentForm
from products.models import Product
from decimal import Decimal
from shortlist.utils import get_shortlist_items_and_total
from django.utils import timezone
from .models import OrderLineItem
from django.contrib import messages
from .utils import save_order_items, charge_card, send_confirmation_email
import stripe
from django.conf import settings

# Create your views here.
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save()
            order.save()
        
            shortlist = request.session.get('shortlist', {})
            save_order_items(order, shortlist)
        
            items_and_total = get_shortlist_items_and_total(shortlist)
            total = items_and_total['shortlist_total']
            stripe_token=payment_form.cleaned_data['stripe_id']

            try:
                customer = charge_card(stripe_token, total)
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.success(request, "You have successfully paid")

                send_confirmation_email(request.user.email, request.user, items_and_total)
        
                del request.session['shortlist']
                return redirect("get_products")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE }
        shortlist = request.session.get('shortlist', {})
        shortlist_items_and_total = get_shortlist_items_and_total(shortlist)
        context.update(shortlist_items_and_total)
    
    return render(request, "checkout/checkout.html", context)
