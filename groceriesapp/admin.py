from django.contrib import admin

# Register your models here.
from .models import Trip, Item, Store, TripItem

admin.site.register(Store)
admin.site.register(Trip)
admin.site.register(Item)

admin.site.register(TripItem)