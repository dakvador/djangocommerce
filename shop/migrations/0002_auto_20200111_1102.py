# Generated by Django 3.0.2 on 2020-01-11 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 11, 2, 38, 149086)),
        ),
    ]