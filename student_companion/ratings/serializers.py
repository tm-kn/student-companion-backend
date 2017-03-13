from django.utils.translation import ugettext_lazy as _
from django.utils.module_loading import import_string

from rest_framework import serializers

from .models import PlaceRating

PublicUserSerializer = import_string('users.serializers.PublicUserSerializer')

class PlaceRatingSerializer(serializers.ModelSerializer):
    user = PublicUserSerializer(read_only=True)
    model = PlaceRating

    class Meta:
        model = PlaceRating
        fields = ['id', 'place', 'user', 'description', 'rating', 'max_rating',
                  'rated_at']
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'place': {
                'read_only': True
            },
            'user': {
                'read_only': True
            },
            'rated_at': {
                'read_only': True
            },
            'max_rating': {
                'read_only': True
            }
        }

    def create(self, validated_data):
        try:
            place_rating = self.model.objects.get(
                place=validated_data['place'],
                user=validated_data['user']
            )
        except PlaceRating.DoesNotExist:
            return self.model.objects.create(**validated_data)
        else:
            place_rating.description = validated_data['description']
            place_rating.rating = validated_data['rating']
            place_rating.rated_at = validated_data['rated_at']
            place_rating.save()
            return place_rating
