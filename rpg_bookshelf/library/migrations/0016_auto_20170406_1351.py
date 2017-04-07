# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 13:51
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_auto_20170406_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_type',
            field=models.IntegerField(choices=[(3, 'Pudełko'), (1, 'Twarda'), (3, 'Ebook'), (2, 'Miękka')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.IntegerField(choices=[(2, 'Dodatek'), (1, 'Podręcznik źródłowy'), (3, 'Inne')]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.ImageField(blank=True, default='media/publisher_logo/brak_logo.jpg', null=True, storage=django.core.files.storage.FileSystemStorage(location='media/publisher_logo'), upload_to=library.models.get_publisher_logo_path),
        ),
    ]
