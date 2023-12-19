from django.urls import path

from .views import GalleryViewSet

gallery_list = GalleryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

gallery_detail = GalleryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('gallery/', gallery_list, name='gallery-list'),
    path('gallery/<int:pk>/', gallery_detail, name='gallery-detail'),
]
