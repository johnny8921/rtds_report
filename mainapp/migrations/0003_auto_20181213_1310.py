# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20181126_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_number', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Заводской номер')),
                ('factory_date', models.DateField(blank=True, null=True, verbose_name='Дата производства')),
                ('work_date', models.DateField(blank=True, null=True, verbose_name='Дата Установки')),
                ('work_number', models.CharField(max_length=5, verbose_name='Номер на поле')),
            ],
        ),
        migrations.AlterField(
            model_name='work',
            name='deviceType',
            field=models.CharField(choices=[('СТР', 'Стелка'), ('ЗАМ', 'Замедлитель'), ('ПЯ', 'Путевой ящик'), ('РИС', 'Измеритель скорости (РИС)')], default='device', max_length=5, verbose_name='Тип устройства'),
        ),
        migrations.AlterField(
            model_name='work',
            name='number',
            field=models.CharField(max_length=5, verbose_name='Номер на поле'),
        ),
        migrations.AlterField(
            model_name='work',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='work',
            name='serialNumber',
            field=models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Серийный номер'),
        ),
        migrations.AlterField(
            model_name='work',
            name='workBody',
            field=models.TextField(verbose_name='Описание работы'),
        ),
        migrations.AlterField(
            model_name='work',
            name='work_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
    ]
