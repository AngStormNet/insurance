# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_data_deduct_limits'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='territory',
            field=models.CharField(default='A', max_length=5),
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='state',
            name='counties',
            field=models.ManyToManyField(editable=False, to='portal.County'),
        ),
    ]
