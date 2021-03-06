# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-29 23:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='image_height', upload_to='places', verbose_name='Image', width_field='image_width')),
                ('image_height', models.PositiveSmallIntegerField(verbose_name='image height')),
                ('image_width', models.PositiveSmallIntegerField(verbose_name='image width')),
            ],
            options={
                'verbose_name': 'place image',
                'verbose_name_plural': 'place images',
            },
        ),
        migrations.AlterField(
            model_name='place',
            name='google_places_id',
            field=models.CharField(blank=True, default=None, max_length=100, unique=True, verbose_name='Google API Place ID'),
        ),
        migrations.AddField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place_images', related_query_name='place_image', to='places.Place', verbose_name='Place'),
        ),
    ]
