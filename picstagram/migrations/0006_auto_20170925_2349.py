# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-26 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picstagram', '0005_auto_20170925_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='caption',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
