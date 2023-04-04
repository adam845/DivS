from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import home_page
from django.urls import path
from product.views import product_list
from news.views import news_list

urlpatterns = [
    path('', home_page, name='home'),
    path('products/', product_list, name='products'),
    path('news/', news_list, name='news'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
