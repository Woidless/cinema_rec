from django.shortcuts import render
from rest_framework import permissions, response
from rest_framework.viewsets import ModelViewSet
from . import serializers
from rating.models import Review
from rating.permissions import IsAuthor
from rest_framework.decorators import action

from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_permissions(self):
        if self.action in ('create',):
            return [permissions.IsAuthenticated()]
        elif self.action in ('update', 'partial_update', 'destroy'):
            return [permissions.IsAuthenticated(), IsAuthor(),]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

