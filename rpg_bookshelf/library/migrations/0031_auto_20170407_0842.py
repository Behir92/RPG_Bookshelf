# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-07 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0030_auto_20170407_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='library/static/cover/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_type',
            field=models.IntegerField(choices=[(1, 'Twarda'), (2, 'Miękka'), (3, 'Pudełko'), (3, 'Ebook')]),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.IntegerField(choices=[(2, 'Dodatek'), (1, 'Podręcznik źródłowy'), (3, 'Inne')]),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='publisher_logo',
            field=models.ImageField(blank=True, null=True, upload_to='library/static/publisher_logo/'),
        ),
        migrations.AlterField(
            model_name='system',
            name='sys_logo',
            field=models.ImageField(blank=True, null=True, upload_to='library/static/sys_logo/'),
        ),
    ]
