from django.db import models
from datetime import datetime

# Create your models here.

class CourseProduct(models.Model):
    course_product_title = models.CharField(max_length=120)
    course_product_description = models.TextField()
    course_product_info = models.TextField()
    course_product_image = models.ImageField(upload_to='store_image/course_product_image/',null=True, blank=True)
    course_product_price = models.IntegerField()
    course_product_status= models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.course_product_title
