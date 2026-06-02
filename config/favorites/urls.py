
from rest_framework.routers import SimpleRouter  # ← بدل DefaultRouter
from .views import FavoriteViewSet # أو اسم الـ view تاعك

router = SimpleRouter()  # ← بدل DefaultRouter
router.register(r'favorite', FavoriteViewSet, basename='favorite')

urlpatterns = router.urls