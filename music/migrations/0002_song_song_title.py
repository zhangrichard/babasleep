# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-13 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]