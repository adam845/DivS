from rest_framework import serializers
from home.models import Home
from product.models import Product
from news.models import News

class HomeSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Home
        fields = '__all__'