# Generated by Django 3.2.13 on 2022-05-19 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_checkpeople_time_delete_timerecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpeople',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 16, 6, 46, 983627)),
        ),
    ]