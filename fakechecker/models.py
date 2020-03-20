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
        return reverse("fakechecker_Expert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_Expert_update", args=(self.pk,))


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
        return reverse("fakechecker_Redactor_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_Redactor_update", args=(self.pk,))


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
        return reverse("fakechecker_QuestionCollection_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_QuestionCollection_update", args=(self.pk,))


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

    DELIMITER = ","

    class Meta:
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("fakechecker_Review_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_Review_update", args=(self.pk,))

    def list_of_sources(self):
        return self.sources.split(self.DELIMITER)


class Category(models.Model):

    # Fields
    name = models.TextField(max_length=100, primary_key=True)
    fa_icon_class = models.TextField(max_length=64, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("fakechecker_Category_detail", args=(self.name,))

    def get_update_url(self):
        return reverse("fakechecker_Category_update", args=(self.name,))


class Question(models.Model):

    # Relationships
    categories = models.ManyToManyField("fakechecker.Category", related_name="questions")

    # Fields
    title = models.TextField(max_length=180)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    sources = models.TextField()

    # Constant
    DELIMITER = ","

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("fakechecker_Question_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_Question_update", args=(self.pk,))

    def list_of_sources(self):
        return self.sources.split(self.DELIMITER)



class QuestionFromUser(Question):

    # Fields
    is_read = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("fakechecker_QuestionFromUser_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_QuestionFromUser_update", args=(self.pk,))


class QuestionForExpert(Question):

    # Relationships
    redactor = models.ForeignKey("fakechecker.Redactor", on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("fakechecker_QuestionForExpert_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("fakechecker_QuestionForExpert_update", args=(self.pk,))

    def get_fake_number(self):
        return self.review_set.filter(is_info_fake=True).count()

    def get_real_number(self):
        return self.review_set.filter(is_info_fake=False).count()

    def get_fake_percentage(self):
        if self.review_set.count() != 0:
            return self.get_fake_number()/self.review_set.count()*100
        return 0
