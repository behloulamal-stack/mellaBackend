from django.db import models
from stores.models import Store
# Create your models here.
class Post(models.Model):
    store = models.ForeignKey(
        Store, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    image = models.ImageField(upload_to='posts/',blank=True , null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # ميزات إضافية
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post by {self.store.name} - {self.created_at.date()}"
    
