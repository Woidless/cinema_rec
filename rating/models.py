from django.db import models

from movie.models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()


class Mark:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    marks = ((one, 'Too bad!'), (two, 'Bad!'), (three, 'Normal!'), (four, 'Good!'), (five, 'Recomended!'))


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField(choices=Mark.marks)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)