from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model 

User = get_user_model()

# Create your models here.
class Products(models.Model):   
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    describe = models.CharField(max_length=555, null=True)
    #photo = models.ImageField(upload_to='images/', null=True, blank=True)
    work_experience = models.CharField(max_length=888, null=True)
    skills = models.CharField(max_length=255, null=True)
    portfolio = models.CharField(max_length=255, null=True)
    contact = models.CharField(max_length=122, null=True)
    testimoni = models.CharField(max_length=266, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 

class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Profiles(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

# Message Class for every user who get delete 
class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    profiles = models.ForeignKey(Profiles, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    describe = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.describe[:50]
