from django.urls import path
from app.mailings.views import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView, MessageView, \
    MessageCreateView, MessageUpdateView, MessageDeleteView, MailingView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, MailingDetailView, MailingSendView

app_name = 'mailings'

urlpatterns = [
    path('client/', ClientView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('message/', MessageView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),

    path('mailings/', MailingView.as_view(), name='mailing_list'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail'),

    path('mailings/<int:pk>/send/', MailingSendView.as_view(), name='mailing_send'),

]
