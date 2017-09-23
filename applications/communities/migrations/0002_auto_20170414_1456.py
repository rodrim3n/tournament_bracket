# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-14 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='players',
            field=models.ManyToManyField(related_name='communities', to='players.Player'),
        ),
    ]