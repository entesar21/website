from rest_framework import serializers
from .models import CourseProduct


class CourseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProduct
        fields = '__all__'

