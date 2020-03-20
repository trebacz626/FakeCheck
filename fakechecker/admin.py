from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django import forms

from . import models


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')}),)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


class ExpertAdminForm(forms.ModelForm):
    class Meta:
        model = models.Expert
        fields = "__all__"


class ExpertAdmin(admin.ModelAdmin):
    form = ExpertAdminForm
    list_display = [
        'user',
        'last_name',
        'first_name',
    ]

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name


class RedactorAdminForm(forms.ModelForm):
    class Meta:
        model = models.Redactor
        fields = "__all__"


class RedactorAdmin(admin.ModelAdmin):
    form = RedactorAdminForm
    list_display = [
        'user',
        'last_name',
        'first_name',
    ]

    def last_name(self, obj):
        return obj.user.last_name

    def first_name(self, obj):
        return obj.user.first_name


class QuestionCollectionAdminForm(forms.ModelForm):
    class Meta:
        model = models.QuestionCollection
        fields = "__all__"


class QuestionCollectionAdmin(admin.ModelAdmin):
    form = QuestionCollectionAdminForm
    list_display = [
        "name",
        "redactor",
        "created",
    ]


class ReviewAdminForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = "__all__"


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = [
        "question_for_expert",
        "expert",
        "is_info_fake",
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
        "name",
    ]


class QuestionFromUserAdminForm(forms.ModelForm):
    class Meta:
        model = models.QuestionFromUser
        fields = "__all__"


class QuestionFromUserAdmin(admin.ModelAdmin):
    form = QuestionFromUserAdminForm
    list_display = [
        "title",
        "categories_list",
        "is_read",
        "created"
    ]


class QuestionForExpertAdminForm(forms.ModelForm):
    class Meta:
        model = models.QuestionForExpert
        fields = "__all__"


class QuestionForExpertAdmin(admin.ModelAdmin):
    form = QuestionForExpertAdminForm
    list_display = [
        "title",
        "categories_list",
        "redactor",
        "created"
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(models.Expert, ExpertAdmin)
admin.site.register(models.Redactor, RedactorAdmin)
admin.site.register(models.QuestionCollection, QuestionCollectionAdmin)
admin.site.register(models.Review, ReviewAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.QuestionFromUser, QuestionFromUserAdmin)
admin.site.register(models.QuestionForExpert, QuestionForExpertAdmin)
