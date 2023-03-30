from django.db import models
from product.models import Product
from news.models import News

class Home(models.Model):
    logo_image = models.ImageField(upload_to='home_images/')
    logo_alt_image = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    news = models.ManyToManyField(News)



def __str__(self):
        return self.logo_alt_image
