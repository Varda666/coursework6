# Generated by Django 4.2.6 on 2023-11-05 17:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0002_alter_mailing_datetime_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='datetime_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 20, 43, 58, 583058), verbose_name='время рассылки с'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='datetime_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 0, 43, 58, 583058), verbose_name='время рассылки до'),
        ),
    ]
