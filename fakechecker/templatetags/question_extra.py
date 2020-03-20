from django import template
from ..models import QuestionForExpert

register = template.Library()

@register.simple_tag
def increment_view(object):
    if type(object) is QuestionForExpert:
        object.increment_view()
    return ""
