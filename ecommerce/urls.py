from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "",
        include("store.urls")
    ),

    path(
        "cart/",
        include("cart.urls")
    ),

    path(
        "orders/",
        include("orders.urls")
    ),

    path(
        "accounts/",
        include("accounts.urls")
    ),

    path(
    "accounts/",
    include("django.contrib.auth.urls")
    ),

    path(

    "api/login/",

    obtain_auth_token,

    name="api_login"

   ),

   path(

    "api/schema/",

    SpectacularAPIView.as_view(),

    name="schema"

),




path(

    "api/docs/",

    SpectacularSwaggerView.as_view(

        url_name="schema"

    ),

    name="swagger-ui"

),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)