from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.db.models import Sum

def register(request):


    if request.method == "POST":

        form = UserCreationForm(
            request.POST
        )


        if form.is_valid():

            form.save()


            return redirect(
                "login"
            )


    else:

        form = UserCreationForm()



    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )

from django.contrib.auth.decorators import login_required



from .forms import ProfileForm





from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.db.models import Sum

from .forms import ProfileForm





@login_required
def profile(request):


    if request.method == "POST":


        form = ProfileForm(

            request.POST,

            request.FILES,

            instance=request.user.profile

        )



        if form.is_valid():


            form.save()


            return redirect(

                "profile"

            )




    else:


        form = ProfileForm(

            instance=request.user.profile

        )






    # DASHBOARD DATA


    total_reviews = request.user.review_set.count()



    wishlist_count = request.user.wishlist.count()



    orders_count = request.user.order_set.count()



    total_spent = request.user.order_set.aggregate(

        Sum("total_price")

    )["total_price__sum"] or 0






    return render(

        request,

        "accounts/profile.html",

        {

            "form": form,


            "total_reviews": total_reviews,


            "wishlist_count": wishlist_count,


            "orders_count": orders_count,


            "total_spent": total_spent,

        }

    )