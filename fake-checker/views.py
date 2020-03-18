from django.views import generic
from . import models
from . import forms


class QuestionCollectionListView(generic.ListView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm


class QuestionCollectionCreateView(generic.CreateView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm


class QuestionCollectionDetailView(generic.DetailView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm


class QuestionCollectionUpdateView(generic.UpdateView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    pk_url_kwarg = "pk"


class ReviewListView(generic.ListView):
    model = models.Review
    form_class = forms.ReviewForm


class ReviewCreateView(generic.CreateView):
    model = models.Review
    form_class = forms.ReviewForm


class ReviewDetailView(generic.DetailView):
    model = models.Review
    form_class = forms.ReviewForm


class ReviewUpdateView(generic.UpdateView):
    model = models.Review
    form_class = forms.ReviewForm
    pk_url_kwarg = "pk"


class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    pk_url_kwarg = "pk"


class QuestionListView(generic.ListView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionCreateView(generic.CreateView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionDetailView(generic.DetailView):
    model = models.Question
    form_class = forms.QuestionForm


class QuestionUpdateView(generic.UpdateView):
    model = models.Question
    form_class = forms.QuestionForm
    pk_url_kwarg = "pk"


class ExpertListView(generic.ListView):
    model = models.Expert
    form_class = forms.ExpertForm


class ExpertCreateView(generic.CreateView):
    model = models.Expert
    form_class = forms.ExpertForm


class ExpertDetailView(generic.DetailView):
    model = models.Expert
    form_class = forms.ExpertForm


class ExpertUpdateView(generic.UpdateView):
    model = models.Expert
    form_class = forms.ExpertForm
    pk_url_kwarg = "pk"


class RedactorListView(generic.ListView):
    model = models.Redactor
    form_class = forms.RedactorForm


class RedactorCreateView(generic.CreateView):
    model = models.Redactor
    form_class = forms.RedactorForm


class RedactorDetailView(generic.DetailView):
    model = models.Redactor
    form_class = forms.RedactorForm


class RedactorUpdateView(generic.UpdateView):
    model = models.Redactor
    form_class = forms.RedactorForm
    pk_url_kwarg = "pk"


class QuestionFromUserListView(generic.ListView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm


class QuestionFromUserCreateView(generic.CreateView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm


class QuestionFromUserDetailView(generic.DetailView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm


class QuestionFromUserUpdateView(generic.UpdateView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    pk_url_kwarg = "pk"


class QuestionForExpertListView(generic.ListView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm


class QuestionForExpertCreateView(generic.CreateView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm


class QuestionForExpertDetailView(generic.DetailView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm


class QuestionForExpertUpdateView(generic.UpdateView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm
    pk_url_kwarg = "pk"
