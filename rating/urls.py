from django.db import router
from django.urls import path, include
from rating.views import ReviewViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('', ReviewViewSet)
urlpatterns = [
     path('', include(router.urls)),
]