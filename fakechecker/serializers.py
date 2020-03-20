from rest_framework import serializers

from . import models


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expert
        fields = [
            "last_updated",
            "profile_pic",
            "about",
            "created",
        ]


class RedactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Redactor
        fields = [
            "phone_number",
            "created",
        ]


class QuestionCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionCollection
        fields = [
            "name",
            "created",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = [
            "last_updated",
            "justification",
            "is_info_fake",
            "created",
            "sources",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = [
            "name",
        ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = [
            "title"
            "content",
            "created",
            "sources",
        ]


class QuestionFromUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionFromUser
        fields = [
            "is_read",
        ]


class QuestionForExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionForExpert
        fields = [
        ]
