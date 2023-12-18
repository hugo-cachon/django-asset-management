from django.http import Http404
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoassetmanagement.image_api.models import Gallery
from djangoassetmanagement.image_api.serializers import GallerySerializer


@permission_classes([AllowAny])
class GalleryList(APIView):
    """
    List all galleries, or create a new gallery.
    """
    def get(self, request, format=None):
        snippets = Gallery.objects.all()
        serializer = GallerySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([AllowAny])
class GalleryDetail(APIView):
    """
    Retrieve, update or delete a gallery instance.
    """
    def get_object(self, pk):
        try:
            return Gallery.objects.get(pk=pk)
        except Gallery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gallery = self.get_object(pk)
        serializer = GallerySerializer(gallery)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gallery = self.get_object(pk)
        serializer = GallerySerializer(gallery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gallery = self.get_object(pk)
        gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)