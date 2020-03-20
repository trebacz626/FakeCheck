from django.db import models
from django.urls import reverse


class Expert(models.Model):

    # Relationships
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    categories = models.ManyToManyField("fakechecker.Category")

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    profile_pic = models.URLField()
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("fake-checker_Expert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Expert_update", args=(self.pk,))


class Redactor(models.Model):

    # Relationships
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

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


class QuestionCollection(models.Model):

    # Relationships
    questions_from_user = models.ManyToManyField("fakechecker.QuestionFromUser")

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
    question_for_expert = models.ForeignKey("fakechecker.QuestionForExpert", on_delete=models.CASCADE)
    expert = models.ForeignKey("fakechecker.Expert", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    justification = models.TextField()
    is_info_fake = models.BooleanField()
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

    # Fields
    name = models.TextField(max_length=100, primary_key=True)

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
    categories = models.ManyToManyField("fakechecker.Category", related_name="questions")

    # Fields
    title = models.TextField(max_length=180)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sources = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("fake-checker_Question_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_Question_update", args=(self.pk,))


class QuestionFromUser(Question):

    # Fields
    is_read = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("fake-checker_QuestionFromUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_QuestionFromUser_update", args=(self.pk,))


class QuestionForExpert(Question):

    # Relationships
    redactor = models.ForeignKey("fakechecker.Redactor", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("fake-checker_QuestionForExpert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fake-checker_QuestionForExpert_update", args=(self.pk,))
