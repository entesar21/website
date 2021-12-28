from django.db import models
from datetime import datetime

# Create your models here.

class Footer(models.Model):
    footer_about_us= models.TextField()
    footer_telegram = models.CharField(max_length=120)
    footer_insta = models.CharField(max_length=120)
    footer_whats_app = models.CharField(max_length=120)
    footer_phone = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)


