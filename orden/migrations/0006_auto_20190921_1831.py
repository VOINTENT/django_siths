# Generated by Django 2.2.5 on 2019-09-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden', '0005_auto_20190921_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sith',
            name='count_h_s',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество рук тени'),
        ),
    ]
