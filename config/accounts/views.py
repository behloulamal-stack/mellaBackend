from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwner
from .serializers import UserSerializer
from .models import User
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated(), IsOwner()]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if 'password' in serializer.validated_data:
            instance.set_password(serializer.validated_data['password'])
            instance.save()
