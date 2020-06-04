# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-04 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_xtheme', '0006_snippets'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='force_to_all_pages',
            field=models.BooleanField(default=False, help_text='Force this snippet to all pages even on the admin page. Do not use for other then meta tags', verbose_name='force_to_all_pages'),
        ),
    ]