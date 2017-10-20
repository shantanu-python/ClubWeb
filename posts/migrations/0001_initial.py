# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 22:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(choices=[('ArtClub', 'ART CLUB'), ('DanceClub', 'DANCE CLUB'), ('MusicClub', 'MUSIC CLUB'), ('CodingClub', 'CODING CLUB'), ('GamingClub', 'GAMING CLUB'), ('PhotographyClub', 'PHOTOGRAPHY CLUB')], max_length=20)),
                ('title', models.CharField(max_length=120)),
                ('information', models.TextField()),
                ('post_time', models.DateTimeField(default=datetime.datetime(2017, 10, 20, 22, 21, 48, 47800, tzinfo=utc))),
            ],
        ),
    ]
