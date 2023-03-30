# Generated by Django 4.1.7 on 2023-03-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_ID', models.AutoField(primary_key=True, serialize=False)),
                ('news_day', models.DateField()),
                ('news_date', models.DateField()),
                ('news_country', models.CharField(max_length=30)),
                ('news_paper', models.CharField(max_length=50)),
                ('news_title', models.CharField(max_length=200)),
                ('news_subtitle', models.CharField(max_length=200)),
                ('news_main_image', models.ImageField(upload_to='news_images/')),
                ('news_main_description', models.TextField()),
                ('news_short_description', models.CharField(max_length=200)),
                ('news_secondary_image', models.ImageField(blank=True, null=True, upload_to='news_images/')),
            ],
        ),
    ]
