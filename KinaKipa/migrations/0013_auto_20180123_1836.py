# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KinaKipa', '0012_auto_20180122_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='news_icon',
            new_name='badge_image',
        ),
    ]
