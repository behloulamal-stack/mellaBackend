from django.db import models

# Create your models here.
from django.db import models
from stores.models import Store

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name =models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price=models.FloatField()
    stock=models.IntegerField()
    is_available=models.BooleanField()
    image_url =models.ImageField(upload_to='products/', null=True, blank=True )
    
    store=models.ForeignKey(Store ,on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return self.product_name