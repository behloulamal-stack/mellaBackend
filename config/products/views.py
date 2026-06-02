from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Product
from .serializers import ProductSerializer
from accounts.permissions import Is_Merchant, IsOwner

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        store_id = self.request.query_params.get('store')
        if store_id:
            queryset = queryset.filter(store__id=store_id)
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [Is_Merchant(), IsOwner()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        store = serializer.validated_data.get('store')
        if store.merchant != self.request.user:  # ✅ merchant بدل owner
            raise PermissionDenied("هذا المحل ماشيش ديالك")
        serializer.save()