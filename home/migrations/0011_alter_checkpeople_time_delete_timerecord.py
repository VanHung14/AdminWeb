# Generated by Django 4.0.2 on 2022-05-19 06:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_checkpeople_time_alter_timerecord_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpeople',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 13, 15, 10, 723407)),
        ),
        migrations.DeleteModel(
            name='TimeRecord',
        ),
    ]
