# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 20:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0011_auto_20171003_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 20, 2, 9, 685863, tzinfo=utc)),
        ),
    ]
