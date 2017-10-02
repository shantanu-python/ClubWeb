# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 14:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0005_auto_20171002_1946'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClubMembers',
            new_name='ClubMember',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 14, 21, 12, 340412, tzinfo=utc)),
        ),
    ]