from rest_framework import serializers
from .models import *

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = "__all__"

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = "__all__"

