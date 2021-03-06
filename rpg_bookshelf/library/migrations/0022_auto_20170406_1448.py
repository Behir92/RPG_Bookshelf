# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0021_auto_20170406_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_type',
            field=models.IntegerField(choices=[(3, 'Pudełko'), (1, 'Twarda'), (2, 'Miękka'), (3, 'Ebook')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.IntegerField(choices=[(2, 'Dodatek'), (3, 'Inne'), (1, 'Podręcznik źródłowy')]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.ImageField(blank=True, default='media/publisher_logo/brak_logo.jpg', null=True, upload_to='library/media'),
        ),
    ]
