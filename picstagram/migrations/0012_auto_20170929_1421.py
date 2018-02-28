# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-29 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picstagram', '0011_pictures_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
