# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KinaKipa', '0020_event_balloon_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='full_description',
        ),
    ]
