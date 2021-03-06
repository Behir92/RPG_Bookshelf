# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-06 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20170406_1353'),
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
            field=models.IntegerField(choices=[(1, 'Podręcznik źródłowy'), (3, 'Inne'), (2, 'Dodatek')]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.ImageField(blank=True, default='media/publisher_logo/brak_logo.jpg', null=True, upload_to='publisher_logo'),
        ),
    ]
