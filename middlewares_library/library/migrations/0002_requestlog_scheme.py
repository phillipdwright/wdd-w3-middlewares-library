# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-09 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlog',
            name='scheme',
            field=models.CharField(default=' ', max_length=10),
            preserve_default=False,
        ),
    ]
