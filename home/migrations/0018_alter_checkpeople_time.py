# Generated by Django 4.0.4 on 2022-06-02 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_checkpeople_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkpeople',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 14, 16, 30, 282046)),
        ),
    ]
