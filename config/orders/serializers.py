from rest_framework import serializers 
from .models import OrderItemModel ,Order
from products.models import Product
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    product_name = serializers.CharField(
        source='product.product_name',
        read_only=True
    )

    price = serializers.FloatField(
        source="product.price",
        read_only=True
    )
    class Meta:
        model =OrderItemModel
        fields = ['id', 'product', 'product_name', 'price', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items =OrderItemSerializer(many=True)
    shop_id = serializers.IntegerField(source='shop.id', read_only=True)
    shop_name = serializers.CharField(source='shop.shop_name', read_only=True)
    customer_name = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'items', 'created_at' ,
                  'shop_id','shop_name' ,'customer_name']
        read_only_fields = ['user', 'total_price', 'created_at']
    def create(self, validated_data):

        items_data = validated_data.pop('items')
        user = self.context['request'].user

        first_product = items_data[0]['product']
        shop = first_product.store

        order = Order.objects.create(
            user=user,
            shop=shop,
            total_price=0
        )

        total_price = 0

        for item_data in items_data:

            product = item_data['product']
            quantity = item_data.get('quantity', 1)

            price = product.price * quantity
            total_price += price

            OrderItemModel.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

        order.total_price = total_price
        order.save()

        return order