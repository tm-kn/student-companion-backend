from rest_framework import serializers

from .models import Place, PlaceCategory, PlaceTag


class SubPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'url')


class SubPlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = ('id', 'url')


class PlaceCategorySerializer(serializers.HyperlinkedModelSerializer):
    category_children = SubPlaceCategorySerializer(many=True, read_only=True)
    place = SubPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = PlaceCategory
        fields = ('id', 'name', 'slug', 'parent', 'category_children', 'place','url')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    categories = SubPlaceCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Place
        fields = ('place_comment', 'place_rating', 'id', 'name', 'slug',
                  'is_visible', 'google_places_id', 'description', 'website',
                  'address', 'telephone_number', 'facebook_handle',
                  'twitter_handle', 'student_discount', 'opening_times',
                  'price_level', 'categories', 'tags', 'url')
