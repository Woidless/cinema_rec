from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from . import serializers
from .models import Genre, Movie


class GenreViewSet(ModelViewSet):
    serializer_class = serializers.GenreSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    queryset = Genre.objects.all()
    search_fields = ['title']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    # pagination_class = StandartResultPagination
    filter_backends = (SearchFilter,)
    search_fields = ('title', )
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('owner', 'genre')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MovieListSerializer
        return serializers.MovieDetailSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
