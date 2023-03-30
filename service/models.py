from django.db import models

class Service(models.Model):
    service_image = models.ImageField(upload_to='service_images/')
    service_title = models.CharField(max_length=200)
    service_description = models.TextField()
    service_foreground = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.service_title
