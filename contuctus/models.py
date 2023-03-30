
from django.db import models

class Contactus(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=200)
    contact_description = models.TextField()
