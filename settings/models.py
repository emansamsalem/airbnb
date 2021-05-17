from django.db import models

# Create your models here.

class Settings(models.Model):
    site_name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="settings/")
    description = models.TextField(max_length=500)
    fb_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    Instagram_link = models.URLField(max_length=200)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=254)


    def __str__(self):
        return self.site_name