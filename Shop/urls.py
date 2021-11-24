from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("",views.index,name = "ShopHome"),
    path("about/",views.about,name = "AboutUS"),
    path("contact/",views.contact,name = "Contact Us"),
    path("tracker/",views.tracker,name = "TrackingStatus"),
    path("search/",views.search,name = "Search"),
    path("productview/",views.productView,name = "ProductView"),
    path("checkout/",views.checkout,name = "Checkout"),
]