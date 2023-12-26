# Generated by Django 4.2.6 on 2023-12-23 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0008_alter_mailing_datetime_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='datetime_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 0, 9, 26, 841192), verbose_name='время рассылки с'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='datetime_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 25, 0, 9, 26, 841192), verbose_name='время рассылки до'),
        ),
    ]
