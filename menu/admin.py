from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Restaurant, Item, ItemGroup, ItemCategory


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('RestaurantName', 'Location', 'UserID')


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('CategoryName', 'RestaurantID')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('ItemName', 'Price', 'RestaurantID', 'ItemGroupID')


class ItemGroupAdmin(admin.ModelAdmin):
    list_display = ('GroupName', 'RestaurantID')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemGroup, ItemGroupAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
