from django import forms
from . import models


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "question",
            "expert",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "questions",
            "expert",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "category",
            "redactor",
        ]


class ExpertForm(forms.ModelForm):
    class Meta:
        model = models.Expert
        fields = [
            "category",
        ]


class RedactorForm(forms.ModelForm):
    class Meta:
        model = models.Redactor
        fields = []

