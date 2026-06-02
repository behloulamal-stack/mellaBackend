from rest_framework import viewsets, permissions
from .models import Post
from stores.models import Store
from .serializers import PostSerializers
from accounts.permissions import Is_Merchant, IsOwner

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [Is_Merchant(), IsOwner()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        store = Store.objects.get(merchant=self.request.user)  # ✅ merchant بدل owner
        serializer.save(store=store)