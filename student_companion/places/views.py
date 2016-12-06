from django.shortcuts import render

from rest_framework import viewsets

from .models import PlaceCategory
from .serializers import PlaceCategorySerializer


class PlaceCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PlaceCategory.objects.all()
    serializer_class = PlaceCategorySerializer
