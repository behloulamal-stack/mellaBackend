from .models import FavoriteModel
from rest_framework import serializers 

class FavoriteSerializer(serializers.ModelSerializer):
    product_name =serializers.CharField(source='product.product_name',read_only=True)
    product_price=serializers.FloatField(source="product.price",read_only=True)

    class Meta:
        model =FavoriteModel 
        fields =['id','product','product_name','product_price','created_at']