from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from rating.serializers import ReviewSerializer
from . import serializers
from .models import Genre, Movie
from rest_framework.decorators import action


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

    #api/v1/products/<id>/reviews/
    @action(['GET', 'POST'], detail=True)
    def reviews(self, request, pk):
        movie = self.get_object()
        if request.method == 'GET':
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return response.Response(serializer.data, status=200)
        if movie.reviews.filter(owner=request.user).exists():
            return response.Response('Вы уже оставляли отзыв!', status=400)
        data = request.data
        serializer = ReviewSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user, movie=movie)
        return response.Response(serializer.data, status=201)

