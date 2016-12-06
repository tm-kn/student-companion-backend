from rest_framework import routers

from places.views import PlaceCategoryViewSet

router = routers.DefaultRouter()
router.register(r'place-categories', PlaceCategoryViewSet)
urlpatterns = router.urls
