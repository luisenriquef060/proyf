# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
