# Generated by Django 2.0.5 on 2018-05-07 04:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 5, 7, 4, 3, 28, 943861, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
