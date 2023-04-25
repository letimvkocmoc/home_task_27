from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from ads.permissions import IsOwner, IsStaff
from ads.serializers import *


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.order_by('name')
    default_serializer_class = SelectionSerializer

    default_permission = [AllowAny]
    permissions = {
        'create': [IsAuthenticated],
        'update': [IsAuthenticated, IsOwner],
        'partial_update': [IsAuthenticated, IsOwner],
        'destroy': [IsAuthenticated, IsOwner]
    }

    serializers = {
        'list': SelectionListSerializer,
        'create': SelectionCreateSerializer,
        'retrieve': SelectionDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
