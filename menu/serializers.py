from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Restaurant, ItemGroup, Item


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['RestaurantName', 'Location', 'UserID']


class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = ['GroupName', 'RestaurantID']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['ItemName', 'Price', 'RestaurantID', 'ItemGroupID']

