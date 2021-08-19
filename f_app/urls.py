from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('register/',views.register ,name="register_url"),
    path('login/',LoginView.as_view() ,name="login_url"),
    path('logout/',LogoutView.as_view(next_page="index"),name='logout'),
    path('',views.home,name="index"),
    path('myaccount/',views.dashboard,name="myaccount"),
    path('shop/',views.shop),
    path('features/',views.features),
    path('blog/',views.blog),
    path('about/',views.about),
    path('Contact/',views.Contact),
    path('search/',views.search),
    path('user/',views.user,name="user"),
]   