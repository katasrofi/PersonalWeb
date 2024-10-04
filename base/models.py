from django.db import models

# Create your models here.
class Product(models.Model):
    url = models.CharField(max_length=555)
    title = models.CharField(max_length=255)
    asin = models.CharField(max_length=100, unique=True)
    price = models.CharField(max_length=30)
    brand = models.CharField(max_length=90)
    product_details = models.TextField(null=True, blank=True)
    breadcrumbs = models.CharField(max_length=255)
    images_list = models.JSONField()
    features = models.JSONField()

    def __str__(self):
        return self.title 
