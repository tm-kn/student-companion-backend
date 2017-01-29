# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-29 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placerating',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_ratings', related_query_name='place_rating', to='places.Place', verbose_name='place'),
        ),
    ]
