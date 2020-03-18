import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Review_list_view():
    instance1 = test_helpers.create_fake-checker_Review()
    instance2 = test_helpers.create_fake-checker_Review()
    client = Client()
    url = reverse("fake-checker_Review_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Review_create_view():
    question = test_helpers.create_fake-checker_Question()
    expert = test_helpers.create_fake-checker_Expert()
    client = Client()
    url = reverse("fake-checker_Review_create")
    data = {
        "question": question.pk,
        "expert": expert.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Review_detail_view():
    client = Client()
    instance = test_helpers.create_fake-checker_Review()
    url = reverse("fake-checker_Review_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Review_update_view():
    question = test_helpers.create_fake-checker_Question()
    expert = test_helpers.create_fake-checker_Expert()
    client = Client()
    instance = test_helpers.create_fake-checker_Review()
    url = reverse("fake-checker_Review_update", args=[instance.pk, ])
    data = {
        "question": question.pk,
        "expert": expert.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_list_view():
    instance1 = test_helpers.create_fake-checker_Category()
    instance2 = test_helpers.create_fake-checker_Category()
    client = Client()
    url = reverse("fake-checker_Category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Category_create_view():
    questions = test_helpers.create_fake-checker_Question()
    expert = test_helpers.create_fake-checker_Expert()
    client = Client()
    url = reverse("fake-checker_Category_create")
    data = {
        "questions": questions.pk,
        "expert": expert.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Category_detail_view():
    client = Client()
    instance = test_helpers.create_fake-checker_Category()
    url = reverse("fake-checker_Category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Category_update_view():
    questions = test_helpers.create_fake-checker_Question()
    expert = test_helpers.create_fake-checker_Expert()
    client = Client()
    instance = test_helpers.create_fake-checker_Category()
    url = reverse("fake-checker_Category_update", args=[instance.pk, ])
    data = {
        "questions": questions.pk,
        "expert": expert.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Question_list_view():
    instance1 = test_helpers.create_fake-checker_Question()
    instance2 = test_helpers.create_fake-checker_Question()
    client = Client()
    url = reverse("fake-checker_Question_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Question_create_view():
    category = test_helpers.create_fake-checker_Category()
    redactor = test_helpers.create_fake-checker_Redactor()
    client = Client()
    url = reverse("fake-checker_Question_create")
    data = {
        "category": category.pk,
        "redactor": redactor.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Question_detail_view():
    client = Client()
    instance = test_helpers.create_fake-checker_Question()
    url = reverse("fake-checker_Question_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Question_update_view():
    category = test_helpers.create_fake-checker_Category()
    redactor = test_helpers.create_fake-checker_Redactor()
    client = Client()
    instance = test_helpers.create_fake-checker_Question()
    url = reverse("fake-checker_Question_update", args=[instance.pk, ])
    data = {
        "category": category.pk,
        "redactor": redactor.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Expert_list_view():
    instance1 = test_helpers.create_fake-checker_Expert()
    instance2 = test_helpers.create_fake-checker_Expert()
    client = Client()
    url = reverse("fake-checker_Expert_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Expert_create_view():
    category = test_helpers.create_fake-checker_Category()
    client = Client()
    url = reverse("fake-checker_Expert_create")
    data = {
        "category": category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Expert_detail_view():
    client = Client()
    instance = test_helpers.create_fake-checker_Expert()
    url = reverse("fake-checker_Expert_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Expert_update_view():
    category = test_helpers.create_fake-checker_Category()
    client = Client()
    instance = test_helpers.create_fake-checker_Expert()
    url = reverse("fake-checker_Expert_update", args=[instance.pk, ])
    data = {
        "category": category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Redactor_list_view():
    instance1 = test_helpers.create_fake-checker_Redactor()
    instance2 = test_helpers.create_fake-checker_Redactor()
    client = Client()
    url = reverse("fake-checker_Redactor_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Redactor_create_view():
    client = Client()
    url = reverse("fake-checker_Redactor_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Redactor_detail_view():
    client = Client()
    instance = test_helpers.create_fake-checker_Redactor()
    url = reverse("fake-checker_Redactor_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Redactor_update_view():
    client = Client()
    instance = test_helpers.create_fake-checker_Redactor()
    url = reverse("fake-checker_Redactor_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302
