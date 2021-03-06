# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 09:27
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_auto_20170406_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_type',
            field=models.IntegerField(choices=[(3, 'Pudełko'), (1, 'Twarda'), (2, 'Miękka'), (3, 'Ebook')]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.ImageField(blank=True, default='media/publisher_logo/brak_logo.jpg', null=True, storage=django.core.files.storage.FileSystemStorage(location='media/publisher_logo'), upload_to=library.models.get_publisher_logo_path),
        ),
    ]
