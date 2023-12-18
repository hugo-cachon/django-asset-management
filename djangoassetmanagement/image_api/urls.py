from django.urls import path
from . import views

urlpatterns = [
    path('gallery/', views.GalleryList.as_view()),
    path('gallery/<int:pk>/', views.GalleryDetail.as_view()),
]
