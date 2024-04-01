from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SerieSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PeliculaSerializer

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimeSerializer
