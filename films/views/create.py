from django.http import JsonResponse
from rest_framework import viewsets
from films.models import Film
from ..serializers import FilmSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """Exibindo todos os filmes"""
    queryset = Film.objects.all()
    serializer_class = FilmSerializer