from django.conf.urls import include, url

from rest_framework import routers

from places.views import PlaceViewSet, PlaceCategoryViewSet
from ratings.views import AddPlaceRatingView

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'place-categories', PlaceCategoryViewSet)
urlpatterns = router.urls

urlpatterns += [
    url(r'^places/(?P<place_id>\d+)/rating/$', AddPlaceRatingView.as_view(),
        name='add-place-rating'),
    url(r'^users/', include('users.urls', namespace='users'))
]
