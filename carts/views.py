from django.shortcuts import render, redirect

from orders.models import Order
from products.models import Product
from .models import Cart

# Create your views here.

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    #This is not efficient method for calculating total since it gets updated after storing in the database or let's say after loading two times
    # products = cart_obj.products.all()
    # total = 0
    # for x in products:
    #     total += x.price
    # print(total)
    # cart_obj.total = total
    # cart_obj.save()
    return render(request, "carts/home.html", {"cart":cart_obj})


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("error")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj) #products can also be added with the help of id as: cart_obj.products.add(1)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    return render(request, "carts/checkout.html", {"object": order_obj})
