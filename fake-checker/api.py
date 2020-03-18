from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for the Review class"""

    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the Category class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Question class"""

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpertViewSet(viewsets.ModelViewSet):
    """ViewSet for the Expert class"""

    queryset = models.Expert.objects.all()
    serializer_class = serializers.ExpertSerializer
    permission_classes = [permissions.IsAuthenticated]


class RedactorViewSet(viewsets.ModelViewSet):
    """ViewSet for the Redactor class"""

    queryset = models.Redactor.objects.all()
    serializer_class = serializers.RedactorSerializer
    permission_classes = [permissions.IsAuthenticated]
