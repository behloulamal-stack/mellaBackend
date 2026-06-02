from rest_framework.routers import SimpleRouter  # ← بدل DefaultRouter
from .views import ProductViewSet

router = SimpleRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls