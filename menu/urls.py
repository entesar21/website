from django.urls import path,include
from .views import *
from rest_framework import routers



urlpatterns = [
    path('show_menu_category/', ShowMenuCategory.as_view()),
    path('add_menu_category/', AddMenuCategory.as_view()),
    path('show_menu_item/', ShowMenuItem.as_view()),
    path('add_menu_item/<int:pk>/', AddMenuItem.as_view()),
]
