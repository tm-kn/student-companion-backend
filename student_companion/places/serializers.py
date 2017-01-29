from rest_framework import serializers

from .models import Place, PlaceCategory, PlaceImage, PlaceTag


class SubPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'url')


class SubPlaceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = ('id', 'name', 'slug', 'url')


class PlaceCategorySerializer(serializers.ModelSerializer):
    category_children = SubPlaceCategorySerializer(many=True, read_only=True)
    place = SubPlaceSerializer(many=True, read_only=True)

    class Meta:
        model = PlaceCategory
        fields = ('id', 'name', 'slug', 'parent', 'category_children', 'place',
                  'url')


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ('id', 'image_height', 'image_width')


class PlaceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceTag
        fields = ('id', 'name')


class PlaceSerializer(serializers.ModelSerializer):
    categories = SubPlaceCategorySerializer(read_only=True, many=True)
    place_images = PlaceImageSerializer(read_only=True, many=True)
    tags = PlaceTagSerializer(read_only=True, many=True)

    class Meta:
        model = Place
        fields = ('place_comments', 'place_ratings', 'id', 'name', 'slug',
                  'is_visible', 'google_places_id', 'description', 'website',
                  'address', 'telephone_number', 'facebook_handle',
                  'twitter_handle', 'student_discount', 'opening_times',
                  'price_level', 'categories', 'tags', 'url', 'place_images')
