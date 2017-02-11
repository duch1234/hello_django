# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wygrzewanie',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('titleClass', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=50)),
                ('type_stb', models.CharField(choices=[('UHD', 'UHD'), ('WHD', 'WHD'), ('Dakota', 'DakotaDakota'), ('WHD/UHD', 'WHD/UHD')], default='WHD/UHD', max_length=20)),
            ],
        ),
    ]
