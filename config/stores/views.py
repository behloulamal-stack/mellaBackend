# from rest_framework.decorators import action
# from urllib import request

# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Store ,Occasion
# from .serializers import StoreSerializers , OccasionSerializers
# from accounts.permissions import Is_Client ,Is_Merchant ,IsOwner
# from rest_framework import permissions
# class OccasionViewSet(viewsets.ModelViewSet):
#     queryset = Occasion.objects.all()
#     serializer_class = OccasionSerializers
#     permission_classes = [permissions.AllowAny]

# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializers

#     def get_permissions(self):
#         if self.action in ['create', 'update', 'partial_update', 'destroy']:
#             return [Is_Merchant(), IsOwner()]
#         if self.action == 'my':
#             return [permissions.AllowAny()]
#         return [permissions.AllowAny()]

#     def perform_create(self, serializer):
#         serializer.save(merchant=self.request.user)  # ✅

#     def get_queryset(self):
#         queryset = Store.objects.all()
#         occasion_id = self.request.query_params.get('occasion_id')
#         if occasion_id:
#             queryset = queryset.filter(occasions__id=occasion_id)
#         return queryset

#     @action(detail=False, methods=['get'])
#     def my(self, request):
#         stores = Store.objects.filter(merchant=request.user)
#         serializer = self.get_serializer(stores, many=True)
#         return Response(serializer.data)
# stores/views.py
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response          # ✅ زيد
from .models import Store, Occasion
from .serializers import StoreSerializers, OccasionSerializers
from accounts.permissions import Is_Merchant, IsOwner


class OccasionViewSet(viewsets.ModelViewSet):
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializers
    permission_classes = [permissions.AllowAny]

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication  # ✅ زيد

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers
    authentication_classes = [JWTAuthentication]  # ✅ زيد صراحة

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), Is_Merchant(), IsOwner()]
        if self.action == 'my':
            return [permissions.IsAuthenticated()]  # ✅
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(merchant=self.request.user)

    def get_queryset(self):
        queryset = Store.objects.all()
        occasion_id = self.request.query_params.get('occasion_id')
        if occasion_id:
            queryset = queryset.filter(occasions__id=occasion_id)
        return queryset
    def perform_create(self, serializer):
        print("=== DATA ===", self.request.data)  # ← زيدي هذا
        print("=== USER ===", self.request.user)
        serializer.save(merchant=self.request.user)

    @action(detail=False, methods=['get'], url_path='my')
    def my(self, request):
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=401)
        stores = Store.objects.filter(merchant=request.user)
        serializer = self.get_serializer(stores, many=True)
        return Response(serializer.data)