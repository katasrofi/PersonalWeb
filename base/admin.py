from django.contrib import admin

# Register your models here.

from .models import Product, Room, Profiles, Messages

admin.site.register(Product)
admin.site.register(Room)
admin.site.register(Profiles)
admin.site.register(Messages)
