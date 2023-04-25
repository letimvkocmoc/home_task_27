from ads.views.selection import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register('', SelectionViewSet)
urlpatterns = router.urls
