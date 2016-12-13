from rest_framework import routers

from places.views import PlaceViewSet, PlaceCategoryViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'place-categories', PlaceCategoryViewSet)
urlpatterns = router.urls
