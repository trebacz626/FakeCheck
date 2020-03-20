from django.contrib.auth.mixins import AccessMixin

from .models import Redactor, Expert, Review, QuestionForExpert

from django.shortcuts import get_object_or_404,redirect


class PermissionMessages:
    general_permission_denied = "Nie masz uprawnień do przeglądania tej treści"


class RoleCheckMixin(AccessMixin):
    permission_denied_message = PermissionMessages.general_permission_denied


class IsExpertMixin(RoleCheckMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            self.expert = request.user.expert
        except Expert.DoesNotExist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class HasExpertAddedReviewMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        self.question_for_expert = get_object_or_404(QuestionForExpert, id=self.kwargs['question_for_expert_id'])
        if Review.objects.filter(expert=self.expert,question_for_expert=self.question_for_expert).first():
            return redirect(self.question_for_expert.get_absolute_url())
        return super().dispatch(request, *args, **kwargs)
