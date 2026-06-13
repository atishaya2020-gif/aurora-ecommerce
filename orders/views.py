from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from cart.models import CartItem

from .models import Order, OrderItem




@login_required
def checkout(request):

    cart_items = CartItem.objects.filter(
        user=request.user
    )
    if not cart_items.exists():

     return redirect("cart")


    total = 0


    for item in cart_items:

        total += item.subtotal()



    order = Order.objects.create(
        user=request.user,
        total_price=total
    )



    for item in cart_items:


        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )


        product = item.product


        product.stock -= item.quantity


        product.save()



    cart_items.delete()



    return redirect("home")





@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    )


    return render(
        request,
        "orders/my_orders.html",
        {
            "orders": orders
        }
    )