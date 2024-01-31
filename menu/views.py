from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item
from .models import Restaurant, ItemGroup, ItemCategory
from .serializers import RestaurantSerializer, ItemGroupSerializer, ItemSerializer, ItemCategorySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ItemGroupViewSet(viewsets.ModelViewSet):
    queryset = ItemGroup.objects.all()
    serializer_class = ItemGroupSerializer


class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


@api_view(['DELETE'])
def delete_multiple_items(request):
    try:
        item_ids = request.query_params.get('item_ids')
        item_ids = [int(_id) for _id in item_ids.split(',')]
        Item.objects.filter(id__in=item_ids).delete()
        print(Item.objects.filter(id__in=item_ids))

        return Response(status=status.HTTP_204_NO_CONTENT)
    except (KeyError, ValueError):
        return Response({"error": "Invalid request data, 'item_ids' not found or not integers"},
                        status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
