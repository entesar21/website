from django.db import models
from datetime import datetime

# Create your models here.

class MenuCategory(models.Model):
    menu_title = models.CharField(max_length=120)
    menu_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['menu_order']

    def __str__(self):
        return self.menu_title


class MenuItem(models.Model):
    menu_item_title = models.CharField(max_length=120)
    menu_item_order = models.IntegerField(default=0)
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE,related_name='menuitem')
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['menu_item_order']

    def __str__(self):
        return self.menu_item_title