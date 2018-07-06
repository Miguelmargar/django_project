from django.contrib import admin
from .models import Order, OrderLineItem

#the below puts OrderLineItem and order in the one section in the admin panel
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )
    
admin.site.register(Order, OrderAdmin)

