"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from menu import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet, 'restaurant')
router.register(r'groups', views.ItemGroupViewSet, 'group')
router.register(r'items', views.ItemViewSet, 'item')
router.register(r'categories', views.ItemCategoryViewSet, 'category')

# Any URL that starts with 'api/' will be handled by the router
# Place custom URLs above the router
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/items/delete_multiple/', views.delete_multiple_items, name='delete_multiple_items'),
    path('api/', include(router.urls)),
]
