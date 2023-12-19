from rest_framework import serializers
from djangoassetmanagement.gallery_api.models import Gallery


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Gallery
        fields = ['url', 'id', 'name', 'owner']

