from rest_framework import serializers
from .models import Kigali

class KigaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kigali
        fields = '__all__'
