# Generated by Django 4.2.6 on 2023-12-23 20:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0006_rename_client_mailingmessage_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='datetime_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 23, 33, 24, 43682), verbose_name='время рассылки с'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='datetime_to',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 23, 33, 24, 43682), verbose_name='время рассылки до'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='frequency',
            field=models.IntegerField(choices=[('once a day', 'once a day'), ('once a week', 'once a week'), ('once a month', 'once a month')], verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.BooleanField(choices=[('completed', 'completed'), ('created', 'created'), ('launched', 'launched')], default=True, verbose_name='статус рассылки'),
        ),
    ]
