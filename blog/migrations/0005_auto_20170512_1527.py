# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 20:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170512_1524'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkbox',
            old_name='image',
            new_name='card',
        ),
    ]
