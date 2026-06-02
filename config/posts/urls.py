from rest_framework import routers
from .views import PostViewSet
router = routers.SimpleRouter()
router.register(r'post', PostViewSet)


urlpatterns = router.urls