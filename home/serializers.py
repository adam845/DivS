from rest_framework import serializers
from product.serializers import ProductSerializer
from news.serializers import NewsSerializer
from .models import Home

class HomeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    news = NewsSerializer(many=True)

    class Meta:
        model = Home
        fields = ['logo_image', 'logo_alt_image', 'products', 'news']
