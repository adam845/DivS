from django.db import models
from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from PIL import Image
from service.models import Service



def validate_image_size(image, width, height):
    img = Image.open(image)
    img_width, img_height = img.size
    if img_width != width or img_height != height:
        raise ValidationError(
            _(f'The image must be {width}px wide and {height}px tall.')
        )

def validate_product_logo(image):
    validate_image_size(image, 200, 88)

def validate_product_background(image):
    validate_image_size(image, 1440, 608)

def validate_product_foreground(image):
    validate_image_size(image, 400, 400)

def validate_product_overview_image(image):
    validate_image_size(image, 300, 380)

def validate_product_feature_image(image):
    validate_image_size(image, 300, 300)

def validate_product_logo_secondary(image):
    validate_image_size(image, 200, 88)
# Create your models here.
class Product(models.Model):
    product_ID = models.AutoField(primary_key=True)
    product_logo = models.ImageField(upload_to='product_images/', validators=[validate_product_logo])
    product_background = models.ImageField(upload_to='product_images/', validators=[validate_product_background])
    product_foreground = models.ImageField(upload_to='product_images/', validators=[validate_product_foreground])
    product_name = models.CharField(max_length=200)
    product_title = models.CharField(max_length=20)
    product_description = models.CharField(max_length=200)
    product_short_description = models.CharField(max_length=100)
    product_services = models.ForeignKey(Service, on_delete=models.CASCADE ,null=True)
    product_overview_title = models.CharField(max_length=200)
    product_overview_description = models.TextField()
    product_overview_image = models.ImageField(upload_to='product_images/', validators=[validate_product_overview_image])
    product_feature_title = models.CharField(max_length=200)
    product_feature_description = models.TextField()
    product_feature_image = models.ImageField(upload_to='product_images/', validators=[validate_product_feature_image])
    product_category = models.IntegerField()
    product_logo_secondary = models.ImageField(upload_to='product_images/', validators=[validate_product_logo_secondary])

    def __str__(self):
        return self.product_name

# Create your models here.

# Create your models here.
