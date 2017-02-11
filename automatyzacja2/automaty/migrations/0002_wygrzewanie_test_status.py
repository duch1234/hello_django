# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automaty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wygrzewanie',
            name='test_Status',
            field=models.CharField(max_length=20, default='done', choices=[('done', 'Wygrzany'), ('not done', 'Nie Wygrzany')]),
        ),
    ]
