from rest_framework import serializers

from . import models


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = [
            "last_updated",
            "created",
        ]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "created",
            "last_updated",
        ]

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = [
            "created",
            "last_updated",
        ]

class ExpertSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Expert
        fields = [
            "last_updated",
            "created",
        ]

class RedactorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Redactor
        fields = [
            "last_updated",
            "created",
        ]
