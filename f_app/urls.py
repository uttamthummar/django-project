from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name="index"),
    path('myaccount/',views.dashboard,name="myaccount"),
    path('shop/',views.shop),
    path('features/',views.features),
    path('blog/',views.blog),
    path('about/',views.about),
    path('Contact/',views.Contact),
    path('search/',views.search),
    path('product_edit/',views.product_edit,name="product_edit"),
    path('list/',views.list),
]   