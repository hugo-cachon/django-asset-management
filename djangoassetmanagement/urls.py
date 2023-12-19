"""
URL configuration for djangoassetmanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from djangoassetmanagement.gallery_api import views as gallery
from djangoassetmanagement.user_api import views as user

# Create a router and register ViewSets with it.
router = DefaultRouter()
router.register(r'gallery', gallery.GalleryViewSet, basename='gallery')
router.register(r'users', user.UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls))
]

