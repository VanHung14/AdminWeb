# Generated by Django 4.0.4 on 2022-05-17 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_timerecord_ok_alter_timerecord_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timerecord',
            old_name='checkFace',
            new_name='checkpeople',
        ),
        migrations.RemoveField(
            model_name='timerecord',
            name='checkRFID',
        ),
        migrations.AlterField(
            model_name='timerecord',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 3, 45, 40, 251982)),
        ),
    ]