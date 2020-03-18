import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

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


def create_fake-checker_Review(**kwargs):
    defaults = {}
    if "question" not in kwargs:
        defaults["question"] = create_fake-checker_Question()
    if "expert" not in kwargs:
        defaults["expert"] = create_fake-checker_Expert()
    defaults.update(**kwargs)
    return fake-checker_models.Review.objects.create(**defaults)
def create_fake-checker_Category(**kwargs):
    defaults = {}
    if "questions" not in kwargs:
        defaults["questions"] = create_fake-checker_Question()
    if "expert" not in kwargs:
        defaults["expert"] = create_fake-checker_Expert()
    defaults.update(**kwargs)
    return fake-checker_models.Category.objects.create(**defaults)
def create_fake-checker_Question(**kwargs):
    defaults = {}
    if "category" not in kwargs:
        defaults["category"] = create_fake-checker_Category()
    if "redactor" not in kwargs:
        defaults["redactor"] = create_fake-checker_Redactor()
    defaults.update(**kwargs)
    return fake-checker_models.Question.objects.create(**defaults)
def create_fake-checker_Expert(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    if "category" not in kwargs:
        defaults["category"] = create_fake-checker_Category()
    defaults.update(**kwargs)
    return fake-checker_models.Expert.objects.create(**defaults)
def create_fake-checker_Redactor(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return fake-checker_models.Redactor.objects.create(**defaults)
