from django.contrib import admin
from .models import Menu, Customer, Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(Menu)
admin.site.register(Cart)