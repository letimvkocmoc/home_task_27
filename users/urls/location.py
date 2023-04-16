from rest_framework import routers

from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)
urlpatterns = router.urls

