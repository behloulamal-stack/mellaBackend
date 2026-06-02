from django.db import models
from accounts.models import User
from products.models import Product
from stores.models import Store
# Create your models here.
class CartModel(models.Model):
    user =models.ForeignKey(User ,on_delete=models.CASCADE)
    shop = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart =models.ForeignKey(CartModel ,on_delete=models.CASCADE)
    product =models.ForeignKey(Product ,on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)