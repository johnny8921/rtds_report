# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20181219_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='state',
            field=models.CharField(choices=[('Установлен', 'Установлен'), ('В запасе', 'В запасе'), ('Есть сбои', 'Есть сбои')], default='В запасе', max_length=25, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='device',
            name='work_station',
            field=models.CharField(choices=[('Четная', 'Четная'), ('Нечетная', 'Нечетная')], default='Четная', max_length=25, verbose_name='Станция установки'),
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата работы'),
        ),
    ]
