# Generated by Django 2.2.5 on 2019-09-21 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': 'Планеты',
            },
        ),
        migrations.CreateModel(
            name='Test_h_s',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Код ордена')),
            ],
            options={
                'verbose_name': 'Тест руки тени',
                'verbose_name_plural': 'Тесты руки тени',
            },
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('count_h_s', models.PositiveSmallIntegerField(default=0, verbose_name='Количество рук тени')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orden.Planet', verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Ситх',
                'verbose_name_plural': 'Ситхи',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('is_passed', models.BooleanField(default=False, verbose_name='Сдал тест?')),
                ('is_h_s', models.BooleanField(default=False, verbose_name='Получил звание руки смерти?')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orden.Planet', verbose_name='Планета')),
            ],
            options={
                'verbose_name': 'Рекрут',
                'verbose_name_plural': 'Рекруты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100, verbose_name='Текст вопроса')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orden.Test_h_s', verbose_name='Код ордена')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('y', 'Да'), ('n', 'Нет')], default='y', max_length=1, verbose_name='Ответ')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden.Question', verbose_name='Вопрос')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden.Recruit', verbose_name='Рекрут')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
