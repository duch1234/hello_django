# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('automaty', '0003_auto_20170211_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='wygrzewanie',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 2, 13, 13, 26, 33, 118728, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='konta_testowe',
            name='accountNumber',
            field=models.PositiveIntegerField(verbose_name='Numer konta', validators=[django.core.validators.MinValueValidator(1000000000, message='Za krótki numer konta. Sprawdz czy numer posiada 10 cyfr'), django.core.validators.MaxValueValidator(9999999999, message='za długi numer konta. Sprawdz czy numer posiada 10 cyfr')]),
        ),
        migrations.AlterField(
            model_name='konta_testowe',
            name='terminalNumbers',
            field=models.DecimalField(verbose_name='Ilość terminali', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], decimal_places=0, default=3, max_digits=1),
        ),
    ]
