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
    path('product_add/',views.product_add,name="product_add"),
    path('product_extend/<int:id>',views.product_extend,name="product_extend"),
    path('product_edit/<int:id>',views.product_edit,name="product_edit"),
    path('product_delete/<int:id>',views.product_delete,name="product_delete"),
    path('list/',views.list),
]   