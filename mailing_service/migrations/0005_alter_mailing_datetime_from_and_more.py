# Generated by Django 4.2.6 on 2023-11-05 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0004_alter_mailing_datetime_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='datetime_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 5, 22, 6, 17, 51559), verbose_name='время рассылки с'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='datetime_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 6, 2, 6, 17, 51559), verbose_name='время рассылки до'),
        ),
        migrations.AlterField(
            model_name='mailingmessage',
            name='client',
            field=models.ManyToManyField(blank=True, related_name='клиенты', to='mailing_service.client'),
        ),
    ]