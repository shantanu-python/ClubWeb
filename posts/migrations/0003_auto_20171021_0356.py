# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 22:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20171021_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 22, 26, 50, 745677, tzinfo=utc)),
        ),
    ]
