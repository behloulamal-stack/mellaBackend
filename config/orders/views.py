from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from rest_framework import permissions
class OrderViewSet(viewsets.ModelViewSet):
    queryset =Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # إرجاع الطلبات الخاصة بالمستخدم فقط
        return Order.objects.filter(user=self.request.user)




class MerchantOrdersViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        shop_id = self.request.query_params.get('shop_id')

        queryset = Order.objects.filter(
            shop__merchant=user
        )

        if shop_id:
            queryset = queryset.filter(shop__id=shop_id)

        return queryset