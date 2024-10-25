from django.contrib import admin

# Register your models here.

from .models import Products, Room, Profiles, Messages

admin.site.register(Products)
admin.site.register(Room)
admin.site.register(Profiles)
admin.site.register(Messages)
