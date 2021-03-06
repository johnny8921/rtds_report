# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20181219_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='state',
            field=models.CharField(choices=[('Есть сбои', 'Есть сбои'), ('В запасе', 'В запасе'), ('Установлен', 'Установлен')], default='В запасе', max_length=25, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='device',
            name='work_station',
            field=models.CharField(choices=[('Нечетная', 'Нечетная'), ('Четная', 'Четная')], default='Четная', max_length=25, verbose_name='Станция установки'),
        ),
    ]
