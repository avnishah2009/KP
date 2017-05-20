from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(db_index=True, max_length=120)
    location = models.CharField(max_length=60, default="Fremont")

    def __str__(self):
        return self.name

class Item(models.Model):
    type_choices = [("Snack", "Snack"),
                    ("Fruit", "Fruit"),
                    ("Vegetable", "Vegetable"),
                    ("Cosmetic", "Cosmetic"),
                    ("Kitchen Item","Kitchen Item"),
                    ("Lentil", "Lentil"),
                    ("Grain", "Grain"),
                    ("Drink","Drink"),
                    ("Dairy", "Dairy"),
                    ("Flour","Flour"),
                    ("Chatni","Chatni"),
                    ("Condiments", "Condiments")]
    name = models.CharField(db_index=True, max_length=100)
    brand = models.CharField(max_length=100, null=True)
    price_per_unit = models.FloatField(null=True)
    unit = models.CharField(max_length=30, null=True)
    type = models.CharField(max_length=32, null=True, choices=type_choices)

    def __str__(self):
        return self.name

class Trip(models.Model):
    date = models.DateField()
    store = models.ForeignKey(Store)
    def __str__(self):
        return  "{0} - {1}".format(self.store.name, self.date.strftime("%m-%d-%Y"))

class TripItem(models.Model):
    trip = models.ForeignKey(Trip)
    item = models.ForeignKey(Item)
    quantity = models.FloatField(null=False, default=0)
    # weight = models.FloatField(null=True, default=0)
    tax = models.FloatField(null=True)

    def __str__(self):
        return  "{0} - {1}".format(self.trip.store.name, self.item)