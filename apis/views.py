from rest_framework import generics

from photos.models import Photo
from .serializers import PhotoSerializer


class PhotoAPIView(generics.ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
