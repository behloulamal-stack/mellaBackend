from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CartItem ,CartModel
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemSerializers

class CartViewSet(ModelViewSet):
    serializer_class = CartItemSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('quantity', 1)

        
        cart, created = CartModel.objects.get_or_create(user=user, shop=product.store)

      
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()