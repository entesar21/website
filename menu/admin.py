from django.contrib import admin

from .models import MenuCategory,MenuItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(MenuCategory)
