from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
#    url = models.CharField(max_length=555)
#    title = models.CharField(max_length=255)
#    asin = models.CharField(max_length=110, unique=True)
#    price = models.CharField(max_length=31)
#    brand = models.CharField(max_length=91)
#    product_details = models.TextField(null=True, blank=True)
#    breadcrumbs = models.CharField(max_length=255)
#    images_list = models.JSONField()
#    features = models.JSONField()
    
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=555, null=True)

    def __str__(self):
        return self.name 

# Message Class for every user who get delete
class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Profiles(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    profiles = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    describe = models.TextField()

    def __str__(self):
        return self.describe[:50]
