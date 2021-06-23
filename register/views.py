from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Menu, Cart
# Create your views here.

def register(request):
    return render(request, 'register/register.html')


def menu(request):
    tablenum = request.POST.get('tablenum', 00)
    phonenum = request.POST.get('phonenum', 00)
    cust = Customer()
    cust.table_num = tablenum
    cust.phone_num = phonenum
    cust.cart_value = 0
    cust.save()
    table_id = Customer.objects.get(table_num = tablenum, phone_num=phonenum).id
    snacks = Menu.objects.filter(category='Snacks')
    return render(request, 'register/menu.html', {'snacks':snacks, 'table_id':table_id})

def add(request, table_id):
    snacks = Menu.objects.filter(category='Snacks')
    item_name = request.POST.get('dish_name', "")
    item_qty = request.POST.get('item_qty', "")
    if(item_qty == 'Half'):
        item_price = Menu.objects.get(dish_name=item_name).dish_half_price
    else:
        item_price = Menu.objects.get(dish_name=item_name).dish_full_price
    item_num = int(request.POST.get('item_num', 1))
    c = Cart()
    c.cart_id = Customer.objects.get(id=table_id)
    c.cart_item = item_name
    c.item_qty = item_qty
    c.item_num = item_num
    c.item_price = item_price
    c.save()
    cust = Customer.objects.get(id=table_id)
    cust.cart_value += (item_price*item_num)
    cust.save()
    return render(request, 'register/menu.html', {'snacks':snacks, 'table_id':table_id})

def payment(request, table_id):
    cart_items = Cart.objects.filter(cart_id_id = table_id)
    cart_total = Customer.objects.get(id=table_id).cart_value
    return render(request, 'register/payment.html', {'cart_items':cart_items, 'totalamt':cart_total})