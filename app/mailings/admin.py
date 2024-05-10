from django.contrib import admin

from app.mailings.models import Mailing, Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'mailing_time', 'duration', 'status')
