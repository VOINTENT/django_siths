from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import RecruitForm, AnswerFormSet, RecruitFormUpdate
from .models import Recruit, Sith, Answer, Question

class IndexView(TemplateView):
    """
    Главная страница
    """
    template_name = 'orden/index.html'

class RecruitCreateView(CreateView):
    """
    Страница отображения формы создания нового рекрута
    """
    template_name = 'orden/create_recruit.html'
    form_class = RecruitForm
    success_url = '{id}/'

def test_view(request, recruit_id):
    """
    Страница отображения списка вопросов
    """
    if request.method == 'POST':
        formset = AnswerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    # Сохранить данные ответы и установить, что рекрут прошел тест
                    current_recruit = Recruit.objects.get(pk=recruit_id)
                    current_recruit.set_passed()
                    answer = Answer(
                        question = form.cleaned_data['question'],
                        recruit = current_recruit,
                        answer = form.cleaned_data['answer']
                    )
                    answer.save()
            return render(request, 'orden/index.html')

    formset = AnswerFormSet(queryset=Recruit.objects.all()[:0], initial=Question.objects.get_initial())
    questions = Question.objects.all()
    context = {'formset' : formset, 'questions' : questions}
    return render(request, 'orden/test.html', context)


class SithListView(ListView):
    """
    Страница отображения списка Ситхов
    """
    template_name = 'orden/sith.html'
    context_object_name = 'siths'

    def get_queryset(self):
        return Sith.objects.all()


def recruits_list_view(request, sith_id):
    """
    Страница отображения списка рекрутов, данных ими ответов и возможности
    присваения каждому из них звания Руки Тени
    """
    if request.method == 'POST':
        rfu = RecruitFormUpdate(request.POST)
        if rfu.is_valid():
            if rfu.cleaned_data:
                # Присвоить рекруту звание
                current_sith = Sith.objects.get(pk=sith_id)
                if current_sith.inc_h_s():
                    recruit = Recruit.objects.get(pk=rfu.cleaned_data['id'])
                    recruit.set_h_s()
                    recruit.save()
                    return HttpResponseRedirect(reverse('recruits_list_view', kwargs = {'sith_id' : sith_id}))

    # Сформировать список рекрутов, ответов и форм для присваения им звания
    recruits = Recruit.objects.get_passed_not_h_s()
    groops_answers = []
    forms = []
    for recruit in recruits:
        groops_answers.append(Answer.objects.filter(recruit=recruit))
        rfu = RecruitFormUpdate(initial = {'id' : recruit.pk})
        forms.append(rfu)

    recruits_answers_forms = zip(recruits, groops_answers, forms)
    context = {'recruits_answers_forms': recruits_answers_forms}

    return render(request, 'orden/recruits.html', context)


class BonusView(TemplateView):
    """
    Страница с бонусным контентом
    Включает в себя отображения списка Ситхов с количеством их Рук Тени и
    списка Ситхов с количеством рук Тени больше 1
    """
    template_name = 'orden/bonus.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['siths_all'] = Sith.objects.all()
        context['siths_gt_1'] = Sith.objects.filter(count_h_s__gt = 1)
        return context
