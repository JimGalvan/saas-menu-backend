from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RestaurantSerializer, ItemGroupSerializer, ItemSerializer
from .models import Restaurant, ItemGroup, Item


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ItemGroupViewSet(viewsets.ModelViewSet):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer