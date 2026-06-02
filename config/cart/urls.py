from rest_framework.routers import SimpleRouter  # ← بدل DefaultRouter
from .views import CartViewSet  # أو اسم الـ view تاعك

router = SimpleRouter()  # ← بدل DefaultRouter
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = router.urls