from django.db.models import Avg
from rest_framework import serializers

from movie.models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Movie
        fields = ('owner', 'title', 'image')



class MovieDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    genre = serializers.PrimaryKeyRelatedField(required=True, queryset=Genre.objects.all())

    class Meta:
        model = Movie
        fields = '__all__'

