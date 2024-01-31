from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant, ItemGroup, Item, ItemCategory


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'RestaurantName', 'Location', 'UserID']


class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = ['GroupName', 'RestaurantID']


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ['id', 'CategoryName', 'RestaurantID']


class ItemSerializer(serializers.ModelSerializer):
    CategoryName = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'ItemName', 'Price', 'RestaurantID', 'ItemGroupID', 'ItemCategoryID', 'CategoryName']

    def get_CategoryName(self, obj):
        if obj.ItemCategoryID is None:
            return None

        return obj.ItemCategoryID.CategoryName  # Assuming 'name' is the field in your Category model

