from django.apps import apps
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions

from .models import PlaceRating
from .serializers import PlaceRatingSerializer

Place = apps.get_model('places', 'Place')

class AddPlaceRatingView(generics.CreateAPIView):
    queryset = PlaceRating.objects.all()
    serializer_class = PlaceRatingSerializer
    permissions = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):
        place = get_object_or_404(Place, id=self.kwargs['place_id'])

        serializer.save(
            place=place,
            user=self.request.user,
            description=self.request.data.get('description', ''),
            rating=self.request.data.get('rating', None)
        )
