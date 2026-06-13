from django.urls import path

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(

    "products",

    views.ProductViewSet

)

urlpatterns = [



    # HOME PAGE

    path(

        "",

        views.home,

        name="home"

    ),







    # PRODUCT DETAIL PAGE

    path(

        "product/<int:product_id>/",

        views.product_detail,

        name="product_detail"

    ),








    # WISHLIST ADD / REMOVE

    path(

        "wishlist/<int:product_id>/",

        views.toggle_wishlist,

        name="toggle_wishlist"

    ),








    # WISHLIST PAGE

    path(

        "wishlist/",

        views.wishlist_page,

        name="wishlist"

    ),









    # ADMIN ANALYTICS

    path(

        "admin-dashboard/",

        views.admin_dashboard,

        name="admin_dashboard"

    ),









    # BASIC FUNCTION BASED API

    path(

        "api/products/",

        views.product_api,

        name="product_api"

    ),










    # DRF GENERIC API
    # GET ALL PRODUCTS
    # CREATE PRODUCT


    path(

        "api/products-new/",

        views.ProductListCreateAPI.as_view(),

        name="products_new"

    ),







    # DRF DETAIL API
    # GET ONE
    # UPDATE
    # DELETE


    path(

        "api/products-new/<int:pk>/",

        views.ProductDetailAPI.as_view(),

        name="product_api_detail"

    ),

    



]


urlpatterns += router.urls

