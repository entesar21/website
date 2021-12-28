from django.db import models

# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=250)
    article_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
