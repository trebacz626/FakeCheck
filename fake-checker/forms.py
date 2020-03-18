from django import forms
from . import models


class ExpertForm(forms.ModelForm):
    class Meta:
        model = models.Expert
        fields = [
            "profile_pic",
            "about",
            "user",
            "category",
        ]


class RedactorForm(forms.ModelForm):
    class Meta:
        model = models.Redactor
        fields = [
            "phone_number",
            "user",
        ]


class QuestionCollectionForm(forms.ModelForm):
    class Meta:
        model = models.QuestionCollection
        fields = [
            "name",
            "question_from_user",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "justification",
            "is_info_fake",
            "sources",
            "question_for_expert",
            "expert",
        ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
            "questions",
            "expert",
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "content",
            "sources",
            "category",
        ]


class QuestionFromUserForm(forms.ModelForm):
    class Meta:
        model = models.QuestionFromUser
        fields = [
            "is_read",
        ]


class QuestionForExpertForm(forms.ModelForm):
    class Meta:
        model = models.QuestionForExpert
        fields = [
            "redactor",
        ]
