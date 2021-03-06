# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20181213_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='state',
            field=models.CharField(choices=[('Есть сбои', 'Есть сбои'), ('В запасе', 'В запасе'), ('Установлен', 'Установлен')], default='В запасе', max_length=25, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='work',
            name='factory_number',
            field=models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Заводской номер'),
        ),
    ]
