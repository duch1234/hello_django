# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automaty', '0002_wygrzewanie_test_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Konta_Testowe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.DecimalField(decimal_places=0, verbose_name='Numer konta', max_digits=10)),
                ('terminalNumbers', models.DecimalField(decimal_places=0, verbose_name='Ilość terminali', max_digits=1)),
                ('technology', models.CharField(choices=[('IPTV', 'IPTV'), ('DTH', 'DTH')], max_length=10, verbose_name='Technologia', default='IPTV')),
                ('accountStatus', models.CharField(choices=[('active', 'Aktywne'), ('not active', 'Nie Aktywne')], max_length=20, verbose_name='Stan konta', default='active')),
            ],
        ),
        migrations.AlterField(
            model_name='wygrzewanie',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='wygrzewanie',
            name='test_Status',
            field=models.CharField(choices=[('done', 'Wygrzany'), ('not done', 'Nie Wygrzany')], max_length=20, verbose_name='Status', default='done'),
        ),
        migrations.AlterField(
            model_name='wygrzewanie',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Nazwa testu'),
        ),
        migrations.AlterField(
            model_name='wygrzewanie',
            name='titleClass',
            field=models.CharField(max_length=300, verbose_name='Nazwa klasy'),
        ),
        migrations.AlterField(
            model_name='wygrzewanie',
            name='type_stb',
            field=models.CharField(choices=[('UHD', 'UHD'), ('WHD', 'WHD'), ('Dakota', 'Dakota'), ('WHD/UHD', 'WHD/UHD')], max_length=20, verbose_name='Typ dekodera', default='WHD/UHD'),
        ),
    ]
