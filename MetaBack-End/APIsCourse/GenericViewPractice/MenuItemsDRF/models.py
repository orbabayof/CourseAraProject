from django.db import models

# Create your models here.
class MenuItemsModel(models.Model):
     title = models.CharField(max_length=255)
     price = models.SmallIntegerField()
     inventory = models.SmallIntegerField()