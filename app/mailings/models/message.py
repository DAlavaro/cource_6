from django.db import models


class Message(models.Model):

    subject = models.CharField(max_length=255, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
