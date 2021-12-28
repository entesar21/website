from django.db import models
from datetime import datetime

# Create your models here.

class Course(models.Model):
    course_title = models.CharField(max_length=120)
    course_description = models.TextField()
    course_info = models.TextField()
    course_image = models.ImageField(upload_to='store_image/courses_image/',null=True, blank=True)
    course_price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.course_title
