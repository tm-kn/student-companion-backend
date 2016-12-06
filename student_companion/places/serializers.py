from rest_framework import serializers

from .models import Place, PlaceCategory, PlaceTag


class BasePlaceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = ('id', 'name', 'slug', 'parent', 'category_children', 'url')


class PlaceCategorySerializer(BasePlaceCategorySerializer):
    category_children = BasePlaceCategorySerializer(many=True, read_only=True)
