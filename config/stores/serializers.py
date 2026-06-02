# stores/serializers.py
from rest_framework import serializers
from .models import Occasion, Store


class OccasionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Occasion
        fields = '__all__'


class StoreSerializers(serializers.ModelSerializer):
    occasions = OccasionSerializers(many=True, read_only=True)
    # ✅ باش تقدر تمرري occasions عند الإنشاء/التعديل
    occasion_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Occasion.objects.all(),
        source='occasions',
        write_only=True,
        required=False,
    )

    class Meta:
        model = Store
        fields = '__all__'
        read_only_fields = ['merchant']   # ✅ merchant يتحدد من perform_create