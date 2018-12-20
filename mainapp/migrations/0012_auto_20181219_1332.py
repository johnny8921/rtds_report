# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20181214_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='author',
        ),
        migrations.RemoveField(
            model_name='work',
            name='deviceType',
        ),
        migrations.RemoveField(
            model_name='work',
            name='number',
        ),
        migrations.RemoveField(
            model_name='work',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='work',
            name='serialNumber',
        ),
        migrations.RemoveField(
            model_name='work',
            name='workBody',
        ),
        migrations.RemoveField(
            model_name='work',
            name='work_date',
        ),
        migrations.AlterField(
            model_name='device',
            name='state',
            field=models.CharField(choices=[('В запасе', 'В запасе'), ('Установлен', 'Установлен'), ('Есть сбои', 'Есть сбои')], default='В запасе', max_length=25, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='device',
            name='work_number',
            field=models.CharField(blank=True, default='', max_length=25, verbose_name='место установки'),
        ),
        migrations.AlterField(
            model_name='device',
            name='work_station',
            field=models.CharField(choices=[('Четная', 'Четная'), ('Нечетная', 'Нечетная')], default='Четная', max_length=25, verbose_name='Станция установки'),
        ),
    ]
