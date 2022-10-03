from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product, Cart, Order, CartItem, ShippingDetails
from authentication.models import Customer


# Create your views here.

def home(request):
    return render(request, 'shop/home_page.html')

def fetch_all_product(request):
    products = Product.objects.all()
    return render(request, 'shop/product_page.html', context={'products' : products})

def fetch_single_product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/product_detail_page.html', context={'product':product})


def cart(request):

    if request.method == 'POST':
        size_id    = request.POST.get('size')
        quantity   = request.POST.get('quantity')

        
        product = get_object_or_404(Product, id=request.POST.get('product_id'))
        customer = Customer.objects.get(id=request.user.id)

        cart, _ = Cart.objects.get_or_create(
            customer=customer
        )

        cartitem, created = CartItem.objects.get_or_create(
            cart=cart,
            item=product,
            quantity=quantity,
            size_id=size_id
        )

        if created:
            cart.cartitem_set.add(cartitem)

        return redirect('home')

    customer = Customer.objects.get(id=request.user.id)
    cart     = get_object_or_404(Cart, customer=customer)

    items = cart.cartitem_set.all()

    return render(request, 'shop/cart_page.html', context={'items' : items})


def checkout(request):
    customer = Customer.objects.get(id=request.user.id)
    cart = get_object_or_404(Cart, customer=customer)

    if request.method == 'POST':

        customer = Customer.objects.get(id=request.user.id)

        shipping, _ = ShippingDetails.objects.get_or_create(
            customer=customer.id,
            adress=request.POST.get('adress')
        )

        order, _ = Order.objects.get_or_create(
            customer=customer,
            cart=cart,
            shipping=shipping,
            completed=False
        )

        return render(request, 'shop/success_page.html')

    return render(request, 'shop/checkout_page.html', context={'cart' : cart})


def list_order(request):
    pass