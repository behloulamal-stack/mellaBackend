# stores/urls.py
from rest_framework import routers          # ✅ زيدي هذا
from .views import OccasionViewSet, StoreViewSet

router = routers.SimpleRouter()
router.register(r'occasion', OccasionViewSet)
router.register(r'store', StoreViewSet)

urlpatterns = router.urls

# appBar: AppBar(
#         title: Image.asset(Assets.logo ,height: 20.sh, ),
#         actions: [
#           IconButton(
#             icon: const Icon(Icons.person_add),
#             onPressed: () {
#               customNavigate(context, AppRoutes.authScreen);
#             },
#           ),
#         ],
#       ),