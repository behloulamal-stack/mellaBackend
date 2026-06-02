from .models import CartItem ,CartModel
from rest_framework import serializers
class CartSrialisers (serializers.ModelSerializer):
    class Meta :
        model =CartModel 
        fields = '__all__'
class CartItemSerializers (serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
    price = serializers.FloatField(source='product.price', read_only=True)
    image_url = serializers.ImageField(source='product.image_url', read_only=True)

    class Meta:
        model=CartItem
        fields = ['id', 'product', 'quantity', 'cart' ,'product_name','price','image_url']  # يمكنك تضمين cart للعرض فقط
        read_only_fields = ['cart'] 



