# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkbox',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Card'),
        ),
    ]
