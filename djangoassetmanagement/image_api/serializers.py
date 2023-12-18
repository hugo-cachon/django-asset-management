from rest_framework import serializers
from djangoassetmanagement.image_api.models import Gallery


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gallery
        fields = ['name']

