from django.urls import path
from shop.views import home, fetch_all_product, fetch_single_product, cart, checkout

urlpatterns = [
    path('', home, name='home'),
    path('products/', fetch_all_product, name='product-list'),
    path('product/<int:id>', fetch_single_product, name='product-details'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout')
]