from ads.views.ad import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', AdViewSet)
urlpatterns = router.urls
