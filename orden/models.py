from django.db import models
from .email import send_message


class RecruitManager(models.Manager):
    # Получить всех рекрутов, прошедших тест, но не получивших звания Руки Тени
    def get_passed_not_h_s(self):
        return Recruit.objects.filter(is_passed=True).filter(is_h_s=False)


class Recruit(models.Model):
    """
    Сущность Рекрут
    Хранит информацию об имени, планете обитания, возрасте, адресе почты, был ли сдан тест
    на Руку Тени и было ли получено звание Руки Смерти. Реализует логику выборки рекрутов и
    уведомления их о присваении звания.
    """
    name = models.CharField(max_length = 50, verbose_name = 'Имя')
    planet = models.ForeignKey('Planet', on_delete = models.PROTECT, verbose_name = 'Планета')
    age = models.PositiveSmallIntegerField(verbose_name = 'Возраст')
    email = models.EmailField(verbose_name = 'Email')
    is_passed = models.BooleanField(default = False, verbose_name = 'Сдал тест?')
    is_h_s = models.BooleanField(default = False, verbose_name = 'Получил звание руки смерти?')

    objects = RecruitManager()

    # Установить, что рекрут сдал тест
    def set_passed(self):
        self.is_passed = True
        self.save()

    # Установить, что рекрут получил звание Руки Тени и уведомить его об этом
    def set_h_s(self):
        self.is_h_s = True
        self.notify()

    # Уведомить рекрута о присваении звании посредствам почты
    def notify(self):
        send_message(self.email)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'


class Sith(models.Model):
    """
    Сущность Ситх
    Хранит информацию об имени Ситха, планете обучения, количестве Рук Тени, реализует логику
    изменения данного количества при присваивании звании новому Рекруту, и ограничивает его (максимум 3).
    Предполагается, что планета обитания рекрута и планета, на которой обучает Ситх, не должны обязательно
    совпадать, так как не было оговорено обратное.
    """
    name = models.CharField(max_length = 50, verbose_name = 'Имя')
    planet = models.ForeignKey('Planet', on_delete = models.PROTECT, verbose_name = 'Планета')
    count_h_s = models.PositiveSmallIntegerField(default = 0, verbose_name = 'Количество рук тени')
    MAX_H_S = 3

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

    # Проверить количество Рук Тени Ситха, и увеличить, если оно меньше 3
    def inc_h_s(self):
        if self.count_h_s < self.MAX_H_S:
            self.count_h_s += 1
            self.save()
            return True
        else:
            return False

    def max(self):
        return self.count_h_s == self.MAX_H_S


class Planet(models.Model):
    """
    Сущность Планета
    Хранит информацию о названии планете.
    """
    name = models.CharField(max_length = 50, verbose_name = 'Планета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'


class Test_h_s(models.Model):
    """
    Сущность Тест Руки Тени
    Хранит информацию о уникальном номере ордена. Является первичной сущностью, на которую
    ссылаются вопросы тест, образуя список.
    """
    code = models.IntegerField(unique = True, verbose_name = 'Код ордена')

    def __str__(self):
        return 'Вопрос ордена %s' % self.code

    class Meta:
        verbose_name = 'Тест руки тени'
        verbose_name_plural = 'Тесты руки тени'


class QuestionManager(models.Manager):
    # Получить список вопросов и вернуть в формате словаря
    def get_initial(self):
        list_initial = []
        questions = Question.objects.all()
        for question in questions:
            list_initial.append({'question' : question})
        return list_initial


class Question(models.Model):
    """
    Сущность Вопрос
    Хранит текст вопроса и ссылку на уникальный номер ордена
    """
    text = models.CharField(max_length = 100, verbose_name = 'Текст вопроса')
    code = models.ForeignKey('Test_h_s', on_delete = models.PROTECT, verbose_name = 'Код ордена')

    objects = QuestionManager()

    def __str__(self):
        if len(self.text) > 37:
            return self.text[:37] + '...'
        return self.text


    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class AnswerManager(models.Manager):
    # Получить все ответы, данные рекрутом
    def get_by_recruit(self, recruit_id):
        recruit = Recruit.objects.get(pk=recruit_id)
        return Answer.objects.filter(recruit=recruit)

class Answer(models.Model):
    """
    Сущность Ответ.
    Хранит информацию об ответе, ссылку на вопрос и ссылку на рекрута, давшего ответ.
    Реализует логику получения всех ответов одного рекрута.
    """
    question = models.ForeignKey('Question', on_delete = models.CASCADE, verbose_name = 'Вопрос')
    recruit = models.ForeignKey('Recruit', on_delete = models.CASCADE, verbose_name = 'Рекрут')
    options = (
        ('y', 'Да'),
        ('n', 'Нет')
    )
    answer = models.CharField(max_length = 1, choices = options, default='y', verbose_name = 'Ответ')

    objects = AnswerManager()

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
