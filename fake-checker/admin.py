from django.contrib import admin
from django import forms

from . import models


class ReviewAdminForm(forms.ModelForm):

    class Meta:
        model = models.Review
        fields = "__all__"


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class QuestionAdminForm(forms.ModelForm):

    class Meta:
        model = models.Question
        fields = "__all__"


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class ExpertAdminForm(forms.ModelForm):

    class Meta:
        model = models.Expert
        fields = "__all__"


class ExpertAdmin(admin.ModelAdmin):
    form = ExpertAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class RedactorAdminForm(forms.ModelForm):

    class Meta:
        model = models.Redactor
        fields = "__all__"


class RedactorAdmin(admin.ModelAdmin):
    form = RedactorAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Expert, ExpertAdmin)
admin.site.register(models.Redactor, RedactorAdmin)
