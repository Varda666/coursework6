from datetime import datetime, timedelta

from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    comment = models.TextField(max_length=300, verbose_name='комментарий')
    user = models.ForeignKey(to='users.User', to_field='email', on_delete=models.PROTECT)

    def __str__(self):
        return self.email, self.first_name, self.last_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailing(models.Model):
    FREQUENCY_CHOISES = [
        ('once a day', 'once a day'),
        ('once a week', 'once a week'),
        ('once a month', 'once a month'),

    ]
    STATUS_CHOISES = [
        ('completed', 'completed'),
        ('created', 'created'),
        ('launched', 'launched'),

    ]
    message = models.ForeignKey(to='MailingMessage', to_field='id', on_delete=models.PROTECT, verbose_name='сообщение')
    datetime_from = models.DateTimeField(default=datetime.now(), verbose_name='время рассылки с')
    datetime_to = models.DateTimeField(default=datetime.now() + timedelta(hours=24), verbose_name='время рассылки до')
    frequency = models.IntegerField(choices=FREQUENCY_CHOISES, verbose_name='периодичность')
    status = models.BooleanField(choices=STATUS_CHOISES, default=True, verbose_name='статус рассылки')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingMessage(models.Model):
    item = models.CharField(max_length=150, verbose_name='тема письма')
    text = models.TextField(verbose_name='тело письма')
    clients = models.ManyToManyField(to='Client', blank=True, related_name='клиенты')
    user = models.ForeignKey(to='users.User', to_field='email', on_delete=models.PROTECT, verbose_name='отправитель')

    def __str__(self):
        return self.item, self.text

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MailingLogs(models.Model):
    mailing = models.ForeignKey(to='Mailing', to_field='id', on_delete=models.PROTECT, verbose_name='рассылка')
    time = models.DateTimeField(verbose_name='время последней попытки')
    status = models.BooleanField(default=False, verbose_name='статус попытки')
    answer_mail_server = models.CharField(max_length=150, default='', verbose_name='ответ почтового сервера')

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
