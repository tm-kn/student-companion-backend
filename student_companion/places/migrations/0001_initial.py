# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('slug', models.SlugField(max_length=30, unique=True, verbose_name='slug')),
                ('is_visible', models.BooleanField(default=False, verbose_name='is visible')),
                ('google_places_id', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Google API Place ID')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('website', models.URLField(blank=True, verbose_name='website')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='formatted address')),
                ('telephone_number', models.CharField(blank=True, max_length=15, verbose_name='formatted telephone number')),
                ('facebook_handle', models.CharField(blank=True, max_length=255, verbose_name='Facebook username')),
                ('twitter_handle', models.CharField(blank=True, max_length=255, verbose_name='Twitter username')),
                ('student_discount', models.CharField(blank=True, max_length=50, verbose_name='student discount')),
                ('opening_times', models.TextField(blank=True, verbose_name='opening hours')),
                ('price_level', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'free'), (1, 'inexpensive'), (2, 'moderate'), (3, 'expensive'), (4, 'very expensive')], null=True, verbose_name='price level')),
            ],
            options={
                'verbose_name': 'place',
                'verbose_name_plural': 'places',
            },
        ),
        migrations.CreateModel(
            name='PlaceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='name')),
                ('slug', models.SlugField(max_length=20, unique=True, verbose_name='slug')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_children', to='places.PlaceCategory', verbose_name='parent category')),
            ],
            options={
                'verbose_name': 'place category',
                'verbose_name_plural': 'place categories',
            },
        ),
        migrations.CreateModel(
            name='PlaceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=10, verbose_name='tag')),
            ],
            options={
                'verbose_name': 'place tag',
                'verbose_name_plural': 'place tags',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='place', to='places.PlaceCategory', verbose_name='categories'),
        ),
        migrations.AddField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(blank=True, to='places.PlaceTag'),
        ),
    ]
