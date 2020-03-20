from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import get_object_or_404, redirect

from FakeCheck import settings
from FakeCheck.settings import MIN_REVIEWS_FOR_PUBLIC_QUESTION
from .models import Redactor, Expert, QuestionForExpert, Review


class PermissionMessages:
    general_permission_denied = "Nie masz uprawnień do przeglądania tej treści"


class RoleCheckMixin(AccessMixin):
    permission_denied_message = PermissionMessages.general_permission_denied


class IsRedactorMixin(RoleCheckMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            redactor = request.user.redactor
        except Redactor.DoesNotExist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsExpertMixin(RoleCheckMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            expert = request.user.expert
        except Expert.DoesNotExist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsRedactorQuestionsAuthorMixin(AccessMixin):
    permission_denied_message = "Nie jesteś autorem tego pytania, więc nie możesz go zmienić!"

    def dispatch(self, request, *args, **kwargs):
        no_permission = True
        question = get_object_or_404(QuestionForExpert, pk=kwargs['pk'])
        question_redactor = question.redactor
        try:
            currently_logged_redactor = request.user.redactor
            no_permission = currently_logged_redactor is question_redactor
        except Redactor.DoesNotExist:
            pass
        if no_permission:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsNumberOfReviewsExceededMixin(AccessMixin):
    permission_denied_message = "Nie możesz zmienić tego pytania ponieważ liczba recenzji które otrzymało jest zbyt duża!"

    def dispatch(self, request, *args, **kwargs):
        question = get_object_or_404(QuestionForExpert, pk=kwargs['pk'])
        if question.reviews.count() >= MIN_REVIEWS_FOR_PUBLIC_QUESTION:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class HasExpertAddedReviewMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        self.question_for_expert = get_object_or_404(QuestionForExpert, id=self.kwargs['question_for_expert_id'])
        if Review.objects.filter(expert=self.expert, question_for_expert=self.question_for_expert).first():
            return redirect(self.question_for_expert.get_absolute_url())
        return super().dispatch(request, *args, **kwargs)
