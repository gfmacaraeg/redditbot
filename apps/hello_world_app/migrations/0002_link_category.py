# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-23 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='category',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
