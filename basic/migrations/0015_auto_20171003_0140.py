# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-02 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0014_auto_20171003_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_name',
            field=models.CharField(choices=[('Art Club', 'ART CLUB'), ('Dance Club', 'DANCE CLUB'), ('Music Club', 'MUSIC CLUB'), ('Coding Club', 'CODING CLUB'), ('Gaming Club', 'GAMING CLUB'), ('Photography Club', 'PHOTOGRAPHY CLUB')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='club_name',
            field=models.CharField(choices=[('Art Club', 'ART CLUB'), ('Dance Club', 'DANCE CLUB'), ('Music Club', 'MUSIC CLUB'), ('Coding Club', 'CODING CLUB'), ('Gaming Club', 'GAMING CLUB'), ('Photography Club', 'PHOTOGRAPHY CLUB')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 2, 20, 10, 10, 39603, tzinfo=utc)),
        ),
    ]
