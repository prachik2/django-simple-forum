# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-05 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_simple_forum', '0002_auto_20160628_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='tags',
            field=models.ManyToManyField(to='django_simple_forum.Tags'),
        ),
    ]