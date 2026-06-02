from django.db import models
from accounts.models import User
from products.models import Product
# Create your models here.
class FavoriteModel (models.Model):
    user =models.ForeignKey(User ,on_delete= models.CASCADE ,related_name='favorites' )
    product =models.ForeignKey(Product,on_delete= models.CASCADE ,related_name='favorited_by')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'product')
        # unique_together يضمن أن كل مستخدم يمكن أن يضيف المنتج مرة واحدة
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
