from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import generic, View

from . import forms
from . import models
from .security import IsRedactorMixin, IsRedactorQuestionCollectionAuthorJSON


class QuestionCollectionListView(generic.ListView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_list.html'


class QuestionCollectionCreateView(IsRedactorMixin,View):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            question_collection = form.save(commit=False)
            question_collection.redactor = request.user.redactor
            question_collection.save()
            return JsonResponse({'message':'success','collection_id':question_collection.pk})
        else:
            return JsonResponse({'error':'please provide valid qyestion collection name'})
    def get(self, request):
        return render(request, 'fakechecker/question_collection_form.html', {
            'question_for_expert_form': forms.QuestionForExpertForm,
        })



class QuestionCollectionDetailView(generic.DetailView):
    model = models.QuestionCollection
    form_class = forms.QuestionCollectionForm
    template_name = 'fakechecker/question_collection_detail.html'

class QuestionCollectionViewQuestion(IsRedactorMixin,
        IsRedactorQuestionCollectionAuthorJSON,View):
    def get_data_from_url(self,request,collection_id,question_id):
        self.question_collection = get_object_or_404(models.QuestionCollection,id=collection_id)
        self.question = get_object_or_404(models.QuestionFromUser,id=question_id)
    def post(self, request, *args, **kwargs):
        self.get_data_from_url(request,kwargs['pk'],kwargs['question_id'])
        self.question_collection.questions_from_user.add(self.question)
        return JsonResponse({'message':'success'})
    def delete(self, request, *args, **kwargs):
        self.get_data_from_url(request,kwargs['pk'],kwargs['question_id'])
        self.question_collection.questions_from_user.remove(self.question)
        return JsonResponse({'message':'success'})
