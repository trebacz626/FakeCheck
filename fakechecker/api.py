from rest_framework import viewsets, permissions

from . import serializers
from . import models


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


class QuestionCollectionViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuestionCollection class"""

    queryset = models.QuestionCollection.objects.all()
    serializer_class = serializers.QuestionCollectionSerializer
    permission_classes = [permissions.IsAuthenticated]


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


class QuestionFromUserViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuestionFromUser class"""

    queryset = models.QuestionFromUser.objects.all()
    serializer_class = serializers.QuestionFromUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionForExpertViewSet(viewsets.ModelViewSet):
    """ViewSet for the QuestionForExpert class"""

    queryset = models.QuestionForExpert.objects.all()
    serializer_class = serializers.QuestionForExpertSerializer
    permission_classes = [permissions.IsAuthenticated]
