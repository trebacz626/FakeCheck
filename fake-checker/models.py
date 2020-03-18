from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Review(models.Model):

    # Relationships
    question = models.ForeignKey("fake-checker.Question", on_delete=models.CASCADE)
    expert = models.ForeignKey("fake-checker.Expert", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_Review_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Review_update", args=(self.pk,))


class Category(models.Model):

    # Relationships
    questions = models.ManyToManyField("fake-checker.Question")
    expert = models.ManyToManyField("fake-checker.Expert")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_Category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Category_update", args=(self.pk,))


class Question(models.Model):

    # Relationships
    category = models.ManyToManyField("fake-checker.Category")
    redactor = models.ForeignKey("fake-checker.Redactor", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_Question_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Question_update", args=(self.pk,))


class Expert(AbstractUser):

    # Relationships
    category = models.ManyToManyField("fake-checker.Category")

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_Expert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Expert_update", args=(self.pk,))


class Redactor(AbstractUser):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_Redactor_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Redactor_update", args=(self.pk,))
