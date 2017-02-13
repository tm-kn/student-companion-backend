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
        read_only_fields = ('name', 'slug', 'url')


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ('id', 'image', 'image_height', 'image_width')


class PlaceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceTag
        fields = ('id', 'name')


class PlaceSerializer(serializers.ModelSerializer):
    categories_data = SubPlaceCategorySerializer(source='categories', read_only=True, many=True)
    place_images = PlaceImageSerializer(read_only=True, many=True)
    tags = PlaceTagSerializer(read_only=True, many=True)

    class Meta:
        model = Place
        fields = ('place_comments', 'place_ratings', 'id', 'name', 'slug',
                  'is_visible', 'google_places_id', 'description', 'website',
                  'address', 'telephone_number', 'facebook_handle',
                  'twitter_handle', 'student_discount', 'opening_times',
                  'price_level', 'categories', 'tags', 'url', 'place_images',
                  'categories_data')
        read_only_fields = ('place_comments', 'place_ratings', 'id', 'name',
                            'slug', 'is_visible', 'description', 'website',
                            'address', 'telephone_number', 'facebook_handle',
                            'twitter_handle', 'opening_times', 'price_level',
                            'tags', 'url', 'place_images', 'categories_data')

    def create(self, validated_data):
        place = Place()
        place.google_places_id = validated_data.get('google_places_id', '')
        place.student_discount = validated_data.get('student_discount', '')
        place.is_visible = False

        place = place.update_data_from_google_api(commit=False)
        place.save()

        place.categories = validated_data.get('categories')
        place.save()

        return place


class PlaceCategorySerializer(serializers.ModelSerializer):
    category_children = SubPlaceCategorySerializer(many=True, read_only=True)
    parent = SubPlaceCategorySerializer(read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = PlaceCategory
        fields = ('id', 'name', 'slug', 'parent', 'category_children',
                  'places', 'url')
