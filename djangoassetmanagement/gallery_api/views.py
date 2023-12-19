from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from djangoassetmanagement.gallery_api.models import Gallery
from djangoassetmanagement.gallery_api.permissions import IsOwnerOrReadOnly
from djangoassetmanagement.gallery_api.serializers import GallerySerializer


@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
class GalleryViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
