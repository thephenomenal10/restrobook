from django.db import models

# Create your models here.
class Customer(models.Model):
    table_num = models.IntegerField()
    phone_num = models.IntegerField()
    cart_value = models.IntegerField()

    def __str__(self):
        return str(self.table_num) + ' -> ' + str(self.cart_value)

class Menu(models.Model):
    dish_name = models.CharField(max_length=50)
    dish_half_price = models.IntegerField(default = 0)
    dish_full_price = models.IntegerField(default = 0)
    category = models.CharField(max_length=20, default='Snacks')

    def __str__(self):
        return self.category + ' -> ' + self.dish_name

class Cart(models.Model):
    cart_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_item = models.CharField(max_length=20)
    item_qty = models.CharField(max_length=4)
    item_num = models.IntegerField()
    item_price = models.IntegerField()
