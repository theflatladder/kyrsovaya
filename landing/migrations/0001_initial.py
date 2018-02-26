# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('surname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=256)),
                ('passwordMatch', models.CharField(max_length=256)),
            ],
        ),
    ]
