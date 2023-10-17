from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
