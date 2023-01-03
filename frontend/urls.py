from django.urls import path
from .views import *
urlpatterns = [
    path('home',index,name = "index"),
    path('',login_request,name = "login"),
    path('register',register_request,name = "register"),
    path('detail/<str:pk>',detail,name = "detail"),
    path('logout',logout_request,name = "logout_request"),
]