from .models import User 
from rest_framework import serializers
from stores.serializers import StoreSerializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # زيد بيانات المستخدم مع التوكن
        data['role'] = self.user.role
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['phone'] = self.user.phone
        data['is_verified'] = self.user.is_verified
        return data

class UserSerializer(serializers.ModelSerializer):
    stores = StoreSerializers(many=True, read_only=True, source="store")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role', 'is_verified', 'stores', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'is_verified': {'read_only': True},
            'stores': {'read_only': True},  # ✅ تأكد أنه read_only
        }
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.role != 'merchant':
            representation.pop('stores', None)
        return representation
    
    def create(self, validated_data):
        # ✅ احذف أي حقل مش موجود في الـ User model
        validated_data.pop('stores', None)
        user = User.objects.create_user(**validated_data)
        return user