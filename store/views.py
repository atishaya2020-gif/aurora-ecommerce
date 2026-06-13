from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from django.db.models import Avg

from .permissions import IsAdminOrReadOnly

from .models import Product, Category

from orders.models import Order

from .forms import ReviewForm

from django.contrib.auth.models import User

from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Count, Sum, Avg

from django.contrib.auth.models import User

from django.contrib.admin.views.decorators import staff_member_required

from django.db.models import Count, Sum, Avg

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import generics

from .serializers import ProductSerializer

from rest_framework import viewsets

from .serializers import ProductSerializer

from .permissions import IsAdminOrReadOnly

def home(request):


    products = Product.objects.annotate(

        average_rating=Avg(
            "reviews__rating"
        )

    )



    categories = Category.objects.all()





    category = request.GET.get(
        "category"
    )



    if category:


        products = products.filter(

            category__id=category

        )






    search = request.GET.get(
        "search"
    )



    if search:


        products = products.filter(

            name__icontains=search

        )







    sort = request.GET.get(
        "sort"
    )



    if sort == "low":


        products = products.order_by(

            "price"

        )



    elif sort == "high":


        products = products.order_by(

            "-price"

        )



    elif sort == "rating":


        products = products.order_by(

            "-average_rating"

        )








    return render(

        request,

        "store/home.html",

        {

            "products": products,


            "categories": categories,

        }

    )








def product_detail(request, product_id):


    product = get_object_or_404(

        Product,

        id=product_id

    )




    reviews = product.reviews.all()




    average_rating = reviews.aggregate(

        Avg("rating")

    )["rating__avg"]





    review_count = reviews.count()






    if request.method == "POST":



        form = ReviewForm(

            request.POST

        )





        if form.is_valid():



            review = form.save(

                commit=False

            )




            review.product = product



            review.user = request.user




            review.save()





            return redirect(

                "product_detail",

                product_id=product.id

            )






    else:


        form = ReviewForm()






    return render(

        request,

        "store/product_detail.html",

        {

            "product": product,


            "reviews": reviews,


            "form": form,


            "average_rating": average_rating,


            "review_count": review_count,

        }

    )









@login_required
def toggle_wishlist(request, product_id):


    product = get_object_or_404(

        Product,

        id=product_id

    )





    if product.wishlist.filter(

        id=request.user.id

    ).exists():



        product.wishlist.remove(

            request.user

        )




    else:



        product.wishlist.add(

            request.user

        )






    return redirect(

        "home"

    )










@login_required
def wishlist_page(request):


    products = request.user.wishlist.all()






    return render(

        request,

        "store/wishlist.html",

        {

            "products": products

        }

    )

@staff_member_required
def admin_dashboard(request):


    total_products = Product.objects.count()


    total_users = User.objects.count()


    total_orders = request.user.order_set.model.objects.count()



    total_revenue = request.user.order_set.model.objects.aggregate(

        Sum("total_price")

    )["total_price__sum"] or 0




    average_rating = Product.objects.aggregate(

        Avg("reviews__rating")

    )["reviews__rating__avg"] or 0





    top_products = Product.objects.annotate(

        review_count=Count("reviews")

    ).order_by(

        "-review_count"

    )[:5]





    return render(

        request,

        "store/admin_dashboard.html",

        {

            "total_products": total_products,

            "total_users": total_users,

            "total_orders": total_orders,

            "total_revenue": total_revenue,

            "average_rating": average_rating,

            "top_products": top_products,

        }

    )

@staff_member_required
def admin_dashboard(request):


    total_products = Product.objects.count()



    total_users = User.objects.count()



    total_orders = Order.objects.count()



    total_revenue = Order.objects.aggregate(

        Sum("total_price")

    )["total_price__sum"] or 0





    average_rating = Product.objects.aggregate(

        Avg("reviews__rating")

    )["reviews__rating__avg"] or 0






    top_products = Product.objects.annotate(

        review_count=Count("reviews")

    ).order_by(

        "-review_count"

    )[:5]







    return render(

        request,

        "store/admin_dashboard.html",

        {


            "total_products": total_products,


            "total_users": total_users,


            "total_orders": total_orders,


            "total_revenue": total_revenue,


            "average_rating": average_rating,


            "top_products": top_products,


        }

    )

# PRODUCT API


@api_view(
    ["GET"]
)
def product_api(request):


    products = Product.objects.all()



    serializer = ProductSerializer(

        products,

        many=True

    )



    return Response(

        serializer.data

    )

# PRODUCT LIST + CREATE API


class ProductListCreateAPI(

    generics.ListCreateAPIView

):


    queryset = Product.objects.all()


    serializer_class = ProductSerializer


    permission_classes = [

        IsAdminOrReadOnly

    ]


    queryset = Product.objects.all()


    serializer_class = ProductSerializer







# PRODUCT DETAIL UPDATE DELETE API


class ProductDetailAPI(

    generics.RetrieveUpdateDestroyAPIView

):


    queryset = Product.objects.all()


    serializer_class = ProductSerializer


    permission_classes = [

        IsAdminOrReadOnly

    ]


    queryset = Product.objects.all()


    serializer_class = ProductSerializer

class ProductViewSet(

    viewsets.ModelViewSet

):


    queryset = Product.objects.all()


    serializer_class = ProductSerializer


    permission_classes = [

        IsAdminOrReadOnly

    ]



    filterset_fields = [

        "category",

        "price",

    ]




    search_fields = [

        "name",

        "description",

    ]




    ordering_fields = [

        "price",

        "stock",

    ]