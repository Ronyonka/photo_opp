# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20190228_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='photos.Category'),
        ),
    ]
