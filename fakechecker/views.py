from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from django.shortcuts import render, redirect, get_object_or_404
from .security import IsRedactorMixin, IsRedactorQuestionsAuthorMixin, IsNumberOfReviewsExceededMixin, \
    HasExpertAddedReviewMixin, IsExpertMixin
from django.contrib.auth import views as auth_views


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


@login_required
def RedactorDetailView(request, pk):
    user = models.Redactor.objects.get(id=pk)
    title = models.QuestionForExpert.objects.filter(redactor=user)
    return render(request, 'fakechecker/redactor_detail.html', {'user': user, 'title': title})


class RedactorUpdateView(generic.UpdateView):
    model = models.Redactor
    form_class = forms.RedactorForm
    pk_url_kwarg = "pk"


class QuestionCollectionListView(generic.ListView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_list.html'


class QuestionCollectionCreateView(generic.CreateView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_form.html'


class QuestionCollectionDetailView(generic.DetailView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_detail.html'


class QuestionCollectionUpdateView(generic.UpdateView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_form.html'
    pk_url_kwarg = "pk"


class ReviewCreateView(IsExpertMixin, HasExpertAddedReviewMixin, generic.CreateView):
    model = models.Review
    form_class = forms.ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['question_for_expert'] = self.question_for_expert
        return context

    def form_valid(self, form, *args, **kwargs):
        question_for_expert = get_object_or_404(models.QuestionForExpert, id=self.kwargs['question_for_expert_id'])
        self.object = form.save(commit=False)
        self.object.question_for_expert = question_for_expert
        self.object.expert = self.expert
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


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


class QuestionFromUserListView(generic.ListView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fakechecker/question_from_user_list.html'

    def get_queryset(self):
        category = self.request.GET.get('category', '')
        is_read = self.request.GET.get('read', '')
        title = self.request.GET.get('title', '')
        order = self.request.GET.get('order', 'created')

        new_context = models.QuestionFromUser.objects.all()
        if category != '':
            new_context = new_context.filter(categories__in=[category])

        if is_read == 'Tylko nowe':
            new_context = new_context.filter(is_read=False)
        elif is_read == 'Tylko przeczytane':
            new_context = new_context.filter(is_read=True)
        if title != '':
            new_context = new_context.filter(title__icontains=title)

        if order == 'Od najnowszego':
            new_context = new_context.order_by('created')
        elif order == 'Od najstarszego':
            new_context = new_context.order_by('-created')

        return new_context

    def get_context_data(self, **kwargs):
        context = super(QuestionFromUserListView, self).get_context_data(**kwargs)
        context['prev_order'] = self.request.GET.get('order', 'created')
        context['prev_read'] = self.request.GET.get('read', '')
        context['prev_category'] = self.request.GET.get('category', '')
        context['title'] = self.request.GET.get('title', '')
        context['orders'] = ('Od najnowszego', 'Od najstarszego')
        context['is_read'] = ('Wszystkie', 'Tylko nowe', 'Tylko przeczytane')
        context['categories'] = models.Category.objects.all()
        return context


class QuestionFromUserCreateView(generic.CreateView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fakechecker/question_from_user_form.html'


class QuestionFromUserDetailView(generic.DetailView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fakechecker/question_from_user_detail.html'


class QuestionFromUserUpdateView(generic.UpdateView):
    model = models.QuestionFromUser
    form_class = forms.QuestionFromUserForm
    template_name = 'fakechecker/question_from_user_form.html'
    pk_url_kwarg = "pk"


class QuestionForExpertListView(generic.ListView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm
    template_name = 'fakechecker/question_for_expert_list.html'

    def get_queryset(self):
        category = self.request.GET.get('category', '')
        title = self.request.GET.get('title', '')
        order = self.request.GET.get('order', 'created')

        new_context = models.QuestionForExpert.objects.all()
        if category != '':
            new_context = new_context.filter(categories__in=[category])

        if title != '':
            new_context = new_context.filter(title__icontains=title)

        if order == 'Od najnowszego':
            new_context = new_context.order_by('created')
        elif order == 'Od najstarszego':
            new_context = new_context.order_by('-created')
        elif order == 'Najpopularniejsze':
            new_context = new_context.order_by('-views')
        elif order == 'Najmniej popularne':
            new_context = new_context.order_by('views')
        elif order == 'Najbardziej oceniane':
            new_context = new_context.annotate(num_reviews=Count('review')).order_by('-num_reviews')
        elif order == 'Najmniej oceniane':
            new_context = new_context.annotate(num_reviews=Count('review')).order_by('num_reviews')

        return new_context

    def get_context_data(self, **kwargs):
        context = super(QuestionForExpertListView, self).get_context_data(**kwargs)
        context['prev_order'] = self.request.GET.get('order', 'created')
        context['title'] = self.request.GET.get('title', '')
        context['prev_read'] = self.request.GET.get('read', '')
        context['prev_category'] = self.request.GET.get('category', '')
        context['orders'] = (
            'Od najnowszego', 'Od najstarszego', 'Najpopularniejsze', 'Najmniej popularne', 'Najbardziej oceniane',
            'Najmniej oceniane')
        context['is_read'] = ('Wszystkie', 'Tylko nowe', 'Tylko przeczytane')
        context['categories'] = models.Category.objects.all()
        return context


class QuestionForExpertCreateView(LoginRequiredMixin, IsRedactorMixin, View):

    def get(self, request):
        return render(request, 'fakechecker/question_for_expert_form.html', {
            'question_for_expert_form': forms.QuestionForExpertForm,
        })

    def post(self, request):
        expert_question = models.QuestionForExpert(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            sources=request.POST.get('sources'),
            redactor=request.user.redactor,
        )
        expert_question.save()
        expert_question.categories.set(request.POST.getlist('categories'))
        return redirect("QuestionForExpert_list")


class QuestionForExpertDetailView(generic.DetailView):
    model = models.QuestionForExpert
    form_class = forms.QuestionForExpertForm
    template_name = 'fakechecker/question_for_expert_detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionForExpertDetailView, self).get_context_data(**kwargs)
        try:
            context['expert_posted'] = context['object'].review_set.filter(expert_id=self.request.user.expert).count()
        except:
            context['expert_posted'] = 0
        return context


class QuestionForExpertUpdateView(LoginRequiredMixin,
                                  IsRedactorMixin,
                                  IsRedactorQuestionsAuthorMixin,
                                  IsNumberOfReviewsExceededMixin,
                                  View):

    def get(self, request, **kwargs):
        object = get_object_or_404(models.QuestionForExpert, pk=kwargs['pk'])
        return render(request, 'fakechecker/question_for_expert_form.html', {
            'question_for_expert_form': forms.QuestionForExpertForm(initial={
                'title': object.title,
                'content': object.content,
                'sources': object.sources,
                'categories': object.categories.all(),
            }),
        })

    def post(self, request, **kwargs):
        expert_question = get_object_or_404(models.QuestionForExpert, pk=kwargs['pk'])
        expert_question.title = request.POST.get('title')
        expert_question.content = request.POST.get('content')
        expert_question.sources = request.POST.get('sources')
        expert_question.save()
        expert_question.categories.set(request.POST.getlist('categories'))
        return redirect("QuestionForExpert_list")


class LoginView(auth_views.LoginView):
    template_name = "fakechecker/login.html"


class LogoutView(auth_views.LogoutView):
    template_name = "fakechecker/logout.html"

    def get_next_page(self):
        next_page = super(LogoutView, self).get_next_page()
        messages.add_message(
            self.request, messages.SUCCESS,
            'You successfully log out!'
        )
        return next_page