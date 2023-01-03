from django.urls import path
from .views import *

urlpatterns = [
    path('',apiurls,name = "apiurls"),
    path('users-list',members,name = "member"),
    path('trans-list',listtrans,name = "translist"),
    path('trans-create',createtrans,name ="createtrans"),
    path('trans-detail/<str:pk>',detailtrans,name = " detailtrans"),
    path('trans-delete/<str:pk>',deletetrans,name = "deletetrans"),
    path('trans-update/<str:pk>',updatetrans,name = "updatetrans"),
]