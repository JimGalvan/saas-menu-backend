from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    RestaurantName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

    # Other restaurant details.

    def __str__(self):
        return self.RestaurantName


class ItemGroup(models.Model):
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    GroupName = models.CharField(max_length=100)

    # Other relevant group details.

    def __str__(self):
        return self.GroupName


class ItemCategory(models.Model):
    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    CategoryName = models.CharField(max_length=100)

    # Other relevant group details.

    def __str__(self):
        return self.CategoryName


class Item(models.Model):
    ItemCategoryID = models.ForeignKey(
        ItemCategory,
        on_delete=models.SET_NULL,  # Change CASCADE to SET_NULL
        null=True,  # Allow null values in the database
        blank=True  # Allow the field to be blank in forms and admin
    )

    ItemGroupID = models.ForeignKey(
        ItemGroup,
        on_delete=models.SET_NULL,  # Change CASCADE to SET_NULL
        null=True,  # Allow null values in the database
        blank=True  # Allow the field to be blank in forms and admin
    )

    RestaurantID = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    ItemName = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=6, decimal_places=2)

    # Other item details.

    def __str__(self):
        return self.ItemName
