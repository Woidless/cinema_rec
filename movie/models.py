from django.db import models
# from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', max_length=100, null=True)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', null=True)
    title = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, related_name='categories', null=True)
    image = models.ImageField(upload_to='images')
    runtime = models.SmallIntegerField()
    actors = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
