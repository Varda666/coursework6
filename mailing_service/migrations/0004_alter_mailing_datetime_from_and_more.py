# Generated by Django 4.2.6 on 2023-11-05 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0003_alter_mailing_datetime_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='datetime_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 22, 5, 20, 441344), verbose_name='время рассылки с'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='datetime_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 2, 5, 20, 441344), verbose_name='время рассылки до'),
        ),
        migrations.RemoveField(
            model_name='mailingmessage',
            name='client',
        ),
        migrations.AddField(
            model_name='mailingmessage',
            name='client',
            field=models.ManyToManyField(to='mailing_service.client', verbose_name='клиент'),
        ),
    ]