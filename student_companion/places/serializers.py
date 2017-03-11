from rest_framework import serializers

from ratings.serializers import PlaceRatingSerializer
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
    categories_data = SubPlaceCategorySerializer(source='categories',
                                                 read_only=True, many=True)
    place_images = PlaceImageSerializer(read_only=True, many=True)
    tags = PlaceTagSerializer(read_only=True, many=True)
    place_ratings = PlaceRatingSerializer(read_only=True, many=True)

    class Meta:
        model = Place
        fields = ('place_comments', 'place_ratings', 'id', 'name', 'slug',
                  'is_visible', 'google_places_id', 'description', 'website',
                  'address', 'telephone_number', 'facebook_handle',
                  'twitter_handle', 'student_discount', 'opening_times',
                  'price_level', 'categories', 'tags', 'url', 'place_images',
                  'categories_data', 'google_maps_url', 'submitted_by')
        extra_kwargs = {
            'place_comments': {'read_only': True},
            'place_ratings': {'read_only': True},
            'id': {'read_only': True},
            'name': {'read_only': True},
            'slug': {'read_only': True},
            'is_visible': {'read_only': True},
            'website': {'read_only': True},
            'address': {'read_only': True},
            'telephone_number': {'read_only': True},
            'facebook_handle': {'read_only': True},
            'twitter_handle': {'read_only': True},
            'opening_times': {'read_only': True},
            'price_level': {'read_only': True},
            'tags': {'read_only': True},
            'url': {'read_only': True},
            'place_images': {'read_only': True},
            'categories_data': {'read_only': True},
            'google_maps_url': {'read_only': True}
        }

    def create(self, validated_data):
        place = Place()
        place.submitted_by = validated_data.get('submitted_by', None)
        place.google_places_id = validated_data.get('google_places_id', '')
        place.student_discount = validated_data.get('student_discount', '')
        place.description = validated_data.get('description', '')
        place.is_visible = False

        place = place.update_data_from_google_api(commit=False)
        place.save()

        place.categories = validated_data.get('categories')
        place.save()

        place.update_images_from_google_api()

        return place


class PlaceCategorySerializer(serializers.ModelSerializer):
    category_children = SubPlaceCategorySerializer(many=True, read_only=True)
    parent = SubPlaceCategorySerializer(read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = PlaceCategory
        fields = ('id', 'name', 'slug', 'parent', 'category_children',
                  'places', 'url')
