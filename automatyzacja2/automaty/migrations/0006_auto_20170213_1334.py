# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automaty', '0005_auto_20170213_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wygrzewanie',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
    ]
