from django.urls import path
from .views import *

urlpatterns = [
    path('show_course_product/', ShowCourseProduct.as_view()),
    path('add_course_product/', AddCourseProduct.as_view()),

]
