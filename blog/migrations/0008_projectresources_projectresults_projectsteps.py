# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-14 03:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_auto_20170513_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110)),
                ('created_ts', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Project')),
                ('resource_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Card')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110)),
                ('created_ts', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Project')),
                ('result_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Card')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSteps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=110)),
                ('step_num', models.IntegerField()),
                ('created_ts', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Project')),
                ('step_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Card')),
            ],
        ),
    ]
