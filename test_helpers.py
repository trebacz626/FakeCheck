import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from fake-checker import models as fake-checker_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_fake-checker_Expert(**kwargs):
    defaults = {}
    defaults["profile_pic"] = ""
    defaults["about"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_User()
    if "category" not in kwargs:
        defaults["category"] = create_fake-checker_Category()
    defaults.update(**kwargs)
    return fake-checker_models.Expert.objects.create(**defaults)
def create_fake-checker_Redactor(**kwargs):
    defaults = {}
    defaults["phone_number"] = ""
    if "user" not in kwargs:
        defaults["user"] = create_User()
    defaults.update(**kwargs)
    return fake-checker_models.Redactor.objects.create(**defaults)
def create_fake-checker_QuestionCollection(**kwargs):
    defaults = {}
    defaults["name"] = ""
    if "question_from_user" not in kwargs:
        defaults["question_from_user"] = create_fake-checker_QuestionFromUser()
    defaults.update(**kwargs)
    return fake-checker_models.QuestionCollection.objects.create(**defaults)
def create_fake-checker_Review(**kwargs):
    defaults = {}
    defaults["justification"] = ""
    defaults["is_info_fake"] = ""
    defaults["sources"] = ""
    if "question_for_expert" not in kwargs:
        defaults["question_for_expert"] = create_fake-checker_QuestionForExpert()
    if "expert" not in kwargs:
        defaults["expert"] = create_fake-checker_Expert()
    defaults.update(**kwargs)
    return fake-checker_models.Review.objects.create(**defaults)
def create_fake-checker_Category(**kwargs):
    defaults = {}
    defaults["name"] = ""
    if "questions" not in kwargs:
        defaults["questions"] = create_fake-checker_Question()
    if "expert" not in kwargs:
        defaults["expert"] = create_fake-checker_Expert()
    defaults.update(**kwargs)
    return fake-checker_models.Category.objects.create(**defaults)
def create_fake-checker_Question(**kwargs):
    defaults = {}
    defaults["content"] = ""
    defaults["sources"] = ""
    if "category" not in kwargs:
        defaults["category"] = create_fake-checker_Category()
    defaults.update(**kwargs)
    return fake-checker_models.Question.objects.create(**defaults)
def create_fake-checker_QuestionFromUser(**kwargs):
    defaults = {}
    defaults["is_read"] = ""
    defaults["content"] = "text"
    defaults["created"] = datetime.now()
    defaults["sources"] = "text"
    defaults.update(**kwargs)
    return fake-checker_models.QuestionFromUser.objects.create(**defaults)
def create_fake-checker_QuestionForExpert(**kwargs):
    defaults = {}
    defaults["content"] = "text"
    defaults["created"] = datetime.now()
    defaults["sources"] = "text"
    if "redactor" not in kwargs:
        defaults["redactor"] = create_fake-checker_Redactor()
    defaults.update(**kwargs)
    return fake-checker_models.QuestionForExpert.objects.create(**defaults)
