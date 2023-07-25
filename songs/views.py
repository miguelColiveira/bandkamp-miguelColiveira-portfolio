from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics


class SongView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        album = get_object_or_404(Album, pk=pk)
        return serializer.save(album=album)

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Song.objects.filter(album_id=pk)
