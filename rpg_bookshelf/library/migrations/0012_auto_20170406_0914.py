# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 09:14
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20170406_0841'),
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
            field=models.IntegerField(choices=[(3, 'Inne'), (1, 'Podręcznik źródłowy'), (2, 'Dodatek')]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.ImageField(blank=True, default='media/publisher_logo/brak_logo.jpg', null=True, storage=django.core.files.storage.FileSystemStorage(location='media/publisher_logo'), upload_to=''),
        ),
    ]
