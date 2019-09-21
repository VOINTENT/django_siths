from django.forms import ModelForm, Form
from django.forms import modelformset_factory, HiddenInput, IntegerField

from .models import Recruit, Question, Answer

class RecruitForm(ModelForm):
    """
    Форма для создания нового рекрута
    """
    class Meta:
        model = Recruit
        fields = ('name', 'planet', 'age', 'email', )


# Набор форм с вопросами и фариантами ответов
def get_afs():
    AnswerFormSet = modelformset_factory(
        Answer,
        fields = ('question', 'answer', ),
        extra = Question.objects.count(),
        widgets = {'question': HiddenInput()}
    )
    return AnswerFormSet


class RecruitFormUpdate(Form):
    """
    Форма для присваения рекруту звания Руки Тени
    """
    id = IntegerField(widget = HiddenInput)
