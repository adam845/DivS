# Generated by Django 4.1.7 on 2023-03-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_product_product_services'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_image', models.ImageField(upload_to='home_images/')),
                ('logo_alt_image', models.CharField(max_length=100)),
                ('news', models.ManyToManyField(to='news.news')),
                ('products', models.ManyToManyField(to='product.product')),
            ],
        ),
    ]
