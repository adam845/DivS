from rest_framework import serializers
from product.serializers import ProductSerializer
from news.serializers import NewsSerializer
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Home
        fields = '__all__'