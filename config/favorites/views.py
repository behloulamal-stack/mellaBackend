from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import FavoriteSerializer
from .models import FavoriteModel
# Create your views here.
class FavoriteViewSet(ModelViewSet):
    serializer_class=FavoriteSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # إرجاع المفضلات الخاصة بالمستخدم
        return FavoriteModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.validated_data['product']

        # الحصول على المفضلة إذا كانت موجودة أو إنشاؤها
        favorite_item, created = FavoriteModel.objects.get_or_create(user=user, product=product)

        # إذا كانت موجودة، لا نغير أي شيء، وإلا سيتم إضافتها
        if not created:
            # يمكنك هنا إرسال رسالة أو تجاهل
            pass
        favorite_item.save()