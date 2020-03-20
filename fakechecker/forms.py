from django import forms
from . import models


class ExpertForm(forms.ModelForm):
    class Meta:
        model = models.Expert
        fields = [
            "profile_pic",
            "about",
            "user",
            "categories",
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
            "questions_from_user",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = [
            "justification",
            "is_info_fake",
            "sources"
        ]
        exclude = ['created','last_updated']
    def clean_sources(self):
        sources = self.cleaned_data.get('sources')
        if (sources.count(' /') > 0 or sources.count('/ ') > 0 or sources.count('i ') > 0 or sources.count(
                ' i') > 0) or (
                len(sources) > 0 and (sources.count('.') == 0 or (sources.count(' ') > 0 and sources.count(',') == 0))):
            raise forms.ValidationError('Zła forma wysłania linków.')
        else:
            return sources


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name",
            "fa_icon_class"
        ]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.QuestionFromUser
        fields = ["title", "content", "categories", "sources"]

    def clean_sources(self):
        sources = self.cleaned_data.get('sources')
        if (sources.count(' /') > 0 or sources.count('/ ') > 0 or sources.count('i ') > 0 or sources.count(
                ' i') > 0) or (
                len(sources) > 0 and (sources.count('.') == 0 or (sources.count(' ') > 0 and sources.count(',') == 0))):
            raise forms.ValidationError('Zła forma wysłania linków.')
        else:
            return sources


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
