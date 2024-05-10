from django.db import models
from app.mailings.models import Client


class Mailing(models.Model):
    STARTED = 'S'
    CREATED = 'C'
    COMPLETED = 'O'
    STATUS_CHOICES = (
        (STARTED, 'Started'),
        (CREATED, 'Created'),
        (COMPLETED, 'Completed'),
    )

    name = models.CharField(max_length=255, verbose_name='Название')
    mailing_time = models.DateTimeField(verbose_name='Время рассылки')
    duration = models.DurationField(verbose_name='Длительность рассылки')
    status = models.CharField(max_length=1, verbose_name='Статус', choices=STATUS_CHOICES, default=CREATED)
    client = models.ManyToManyField(Client, verbose_name='Клиенты')
    message = models.ForeignKey('Message', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cообщение')

    def __str__(self):
        return f'{self.mailing_time} - {self.duration} - {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
