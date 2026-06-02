from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id', 'product_name', 'description',
            'price', 'stock', 'is_available', 'image_url',
            'store'  
        ]