
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
    home = Home.objects.first()  # retrieve a single instance of Home
    products = Product.objects.all()
    news = News.objects.all()
    home_serializer = HomeSerializer(home)
    product_serializer = ProductSerializer(products, many=True)
    news_serializer = NewsSerializer(news, many=True)
    data = {
        'home': home_serializer.data,
        'products': product_serializer.data,
        'news': news_serializer.data
    }
    return Response(data)
