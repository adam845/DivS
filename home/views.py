from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from news.models import News
from product.serializers import ProductSerializer
from news.serializers import NewsSerializer

@api_view(['GET'])
def home_page(request):
    products = Product.objects.all()
    news = News.objects.all()
    product_serializer = ProductSerializer(products, many=True)
    news_serializer = NewsSerializer(news, many=True)
    data = {
        'products': product_serializer.data,
        'news': news_serializer.data
    }
    return Response(data)

# Create your views here.
