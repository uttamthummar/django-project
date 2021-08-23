from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [

    path('',views.home,name="index"),
    path('myaccount/',views.dashboard,name="myaccount"),
    path('shop/',views.shop),
    path('features/',views.features),
    path('blog/',views.blog),
    path('about/',views.about),
    path('Contact/',views.Contact),
    path('search/',views.search),
]   