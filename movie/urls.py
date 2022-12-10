from django.urls import path, include
from rest_framework.routers import SimpleRouter

from movie.views import MovieViewSet, GenreViewSet


router = SimpleRouter()
router.register('movies', MovieViewSet)
router.register('genres', GenreViewSet)
urlpatterns = [
     path('', include(router.urls)),
]