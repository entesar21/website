from rest_framework import serializers
from .models import MenuItem,MenuCategory




class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = MenuItem
        fields = '__all__'



class MenuCategorySerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True, many=True)
    class Meta:
        model = MenuCategory
        fields = '__all__'

    # def create(self, validated_data):
    #     menuitems = validated_data.pop('tracks')
    #     category = MenuCategory.objects.create(**validated_data)
    #     for menuitem in menuitems:
    #         MenuItem.objects.create(category=category, **menuitem)
    #     return category




