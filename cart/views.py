from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.models import Product
from .models import CartItem

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )


    if product.stock <= 0:

        return redirect("home")



    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )



    if not created:

        if cart_item.quantity < product.stock:

            cart_item.quantity += 1

            cart_item.save()



    return redirect("home")


@login_required
def view_cart(request):

    items = CartItem.objects.filter(
        user=request.user
    )


    total = 0


    for item in items:

        total += item.subtotal()


    return render(
        request,
        "cart/cart.html",
        {
            "items": items,
            "total": total
        }
    )

@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )


    item.delete()


    return redirect("cart")