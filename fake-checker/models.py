from django.db import models
from django.urls import reverse


class QuestionCollection(models.Model):

    # Relationships
    question_from_user = models.ManyToManyField("fake-checker.QuestionFromUser")

    # Fields
    name = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("fake-checker_QuestionCollection_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_QuestionCollection_update", args=(self.pk,))


class Review(models.Model):

    # Relationships
    question_for_expert = models.ForeignKey("fake-checker.QuestionForExpert", on_delete=models.CASCADE)
    expert = models.ForeignKey("fake-checker.Expert", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    justification = models.TextField()
    is_legit = models.BinaryField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sources = models.TextField()

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
    name = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("fake-checker_Category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Category_update", args=(self.pk,))


class Question(models.Model):

    # Relationships
    category = models.ManyToManyField("fake-checker.Category")

    # Fields
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sources = models.TextField()

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
    profile_pic = models.URLField()
    about = models.TextField()
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
    phone_number = models.TextField(max_length=12)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_Redactor_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Redactor_update", args=(self.pk,))


class QuestionFromUser(Question):

    # Fields
    is_read = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_QuestionFromUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_QuestionFromUser_update", args=(self.pk,))


class QuestionForExpert(Question):

    # Relationships
    redactor = models.ForeignKey("fake-checker.Redactor", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fake-checker_QuestionForExpert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_QuestionForExpert_update", args=(self.pk,))
