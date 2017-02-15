# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automaty', '0004_auto_20170213_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wygrzewanie',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
