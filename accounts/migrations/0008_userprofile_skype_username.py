# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_add_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='skype_username',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
