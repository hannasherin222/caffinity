from django.contrib import admin

# Register your models here.
from .models import Brewbella,Cart,Orders


class BrewbellaAdmin(admin.ModelAdmin):
    list_display=['id','name','quantity','price']


class CartAdmin(admin.ModelAdmin):
    list_display=['id','productid','user','productname','proprice','productquantity','total'
    ]



class OrderAdmin(admin.ModelAdmin):
    list_display=[
    'phoneno',
    'address',
    'city',
    'state',
    'pincode',
    'email',
    'tamount',
    'razorpay_order_id']

admin.site.register(Brewbella,BrewbellaAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(Orders,OrderAdmin)