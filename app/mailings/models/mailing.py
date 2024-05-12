from django.db import models
from app.mailings.models import Client


class Mailing(models.Model):
    name = models.CharField(max_length=100, verbose_name='название рассылки')
    start_time = models.DateTimeField(verbose_name='время начала отправки рассылки')
    end_time = models.DateTimeField(verbose_name='время окончания отправки рассылки')

    daily = 'раз в день'
    weekly = 'раз в неделю'
    monthly = 'раз в месяц'
    Periodicity = [
        (daily, 'раз в день'),
        (weekly, 'раз в неделю'),
        (monthly, 'раз в месяц')
    ]
    periodicity = models.CharField(max_length=20,verbose_name='периодичность',choices=Periodicity)


    finished = 'завершена'
    created = 'создана'
    launched = 'запущена'
    Status = [
        (finished, 'завершена'),
        (created, 'создана'),
        (launched, 'запущена')
    ]
    status = models.CharField(max_length=20,verbose_name='статус рассылки',choices=Status,default=created)

    client = models.ManyToManyField(Client, verbose_name='Клиенты')
    message = models.ForeignKey('Message', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
