# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-09-20 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField()),
            ],
        ),
    ]
