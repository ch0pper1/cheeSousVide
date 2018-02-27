# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheeseIt', '0002_cheese_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheese',
            name='holdTime',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='name',
            field=models.CharField(default='Cheeeeeeeese', max_length=64, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='cheese',
            name='onTemp',
            field=models.BooleanField(default=False),
        ),
    ]