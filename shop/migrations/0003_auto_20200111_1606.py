# Generated by Django 3.0.2 on 2020-01-11 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200111_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 11, 16, 6, 15, 75495)),
        ),
    ]
