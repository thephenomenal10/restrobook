from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    #/register/
    path('', views.register, name='register'),
    #/register/menu/
    path('/menu/', views.menu, name='menu'),
    #/register/add/table_id/
    path('/add/<int:table_id>', views.add, name="add_to_cart"),
    #/payment/table_id
    path('/<int:table_id>', views.payment, name='payment')
]
