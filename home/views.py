from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Home
from .serializers import HomeSerializer
from product.models import Product
from news.models import News
from product.serializers import ProductSerializer
from news.serializers import NewsSerializer

@api_view(['GET'])
def home_page(request):
    home = Home.objects.all().first()
    serializer = HomeSerializer(home)
    return Response(serializer.data)