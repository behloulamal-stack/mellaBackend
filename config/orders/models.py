from django.db import models
from accounts.models import User
from products.models import Product
from stores.models import Store
# Create your models here.
class Order(models.Model):
    STATUS_CHOICES =[
         ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),

    ]
    user =models.ForeignKey(User ,on_delete=models.CASCADE)
    shop = models.ForeignKey(
    Store,
    on_delete=models.CASCADE,
    related_name="orders"
)
    total_price=models.FloatField()
    status =models.CharField( max_length=20,choices=STATUS_CHOICES ,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    
class OrderItemModel(models.Model):
    order =models.ForeignKey(Order,on_delete=models.CASCADE ,related_name='items')
    product =models.ForeignKey(Product ,on_delete=models.CASCADE)
    quantity =models.PositiveIntegerField(default=1)
    price =models.FloatField()
    def __str__(self):
       return f"{self.quantity} x {self.product.product_name}"
