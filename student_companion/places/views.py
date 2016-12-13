from django.shortcuts import render

from rest_framework import viewsets

from .models import Place, PlaceCategory
from .serializers import PlaceSerializer, PlaceCategorySerializer


class PlaceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlaceCategory.objects.all()
    serializer_class = PlaceCategorySerializer


class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
