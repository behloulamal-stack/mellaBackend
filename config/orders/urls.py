from rest_framework import routers
from .views import OrderViewSet ,MerchantOrdersViewSet
router = routers.SimpleRouter()
router.register(r'order', OrderViewSet)
router.register(r'merchant-orders', MerchantOrdersViewSet, basename='merchant-orders')


urlpatterns = router.urls