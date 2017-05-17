# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_add_userskill_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=100)),
                ('field_of_study', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.School'),
        ),
    ]
