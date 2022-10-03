from django.contrib import admin
from shop.models import Color, Size, Image, Product, Cart, CartItem, Order, ShippingDetails
# Register your models here.

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingDetails)