from rest_framework import permissions, viewsets, mixins, status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated

from .models import Place, PlaceCategory
from .serializers import PlaceSerializer, PlaceCategorySerializer
from users.serializers import UserSerializer


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



    @list_route()
    def bookmarked(self, request):
        if not request.user.is_authenticated():
            raise NotAuthenticated

        places = request.user.bookmarked_places.all()

        place_serializer = PlaceSerializer(places, many=True, read_only=True,
                                           context={'request': request})

        return Response(place_serializer.data)

    @detail_route(methods=['post'])
    def bookmark(self, request, pk=None):
        request.user.bookmarked_places.add(self.get_object())

        user = UserSerializer(request.user, context={'request': request})

        return Response(user.data,
                        status.HTTP_201_CREATED)

    @detail_route(methods=['post'])
    def unbookmark(self, request, pk=None):
        request.user.bookmarked_places.remove(self.get_object())

        user = UserSerializer(request.user,  context={'request': request})

        return Response(user.data,
                        status.HTTP_201_CREATED)
