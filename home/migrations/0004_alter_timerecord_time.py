# Generated by Django 4.0.4 on 2022-04-26 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_timerecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timerecord',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 26, 23, 45, 6, 136449)),
        ),
    ]
