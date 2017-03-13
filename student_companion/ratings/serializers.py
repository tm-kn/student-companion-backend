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
        if PlaceRating.objects.filter(place=validated_data['place'], user=validated_data['user']).exists():
            raise serializers.ValidationError({'detail': _('You have already rated this place')})

        return self.model.objects.create(**validated_data)
