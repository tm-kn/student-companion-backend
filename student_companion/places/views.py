from django.shortcuts import render

from rest_framework import permissions, viewsets, mixins

from .models import Place, PlaceCategory
from .serializers import PlaceSerializer, PlaceCategorySerializer


class PlaceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlaceCategory.objects.all()
    serializer_class = PlaceCategorySerializer


class PlaceViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.visible()
    serializer_class = PlaceSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get_queryset(self):
        search_string = self.request.query_params.get('search_string', None)

        if search_string:
            return self.queryset.search(search_string)

        return self.queryset

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)
