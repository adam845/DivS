from django.db import models

class News(models.Model):
    news_ID = models.AutoField(primary_key=True)
    news_day = models.DateField()
    news_date = models.DateField()
    news_country = models.CharField(max_length=30)
    news_paper = models.CharField(max_length=50)
    news_title = models.CharField(max_length=200)
    news_subtitle = models.CharField(max_length=200)
    news_main_image = models.ImageField(upload_to='news_images/')
    news_main_description = models.TextField()
    news_short_description = models.CharField(max_length=200)
    news_secondary_image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.news_title