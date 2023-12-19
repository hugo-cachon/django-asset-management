from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    galleries = serializers.HyperlinkedRelatedField(many=True,
                                                    view_name='gallery-detail',
                                                    read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'galleries']

