from django.db import models
from accounts.models import User
# Create your models here.
class Occasion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='occasions/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Store(models.Model):

    merchant = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='store'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # الموقع الجغرافي
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    
    # العلاقة مع المناسبات (متعدد لمتعدد)
    occasions = models.ManyToManyField(Occasion, related_name='stores')
    logo = models.ImageField(upload_to='store_logos/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name