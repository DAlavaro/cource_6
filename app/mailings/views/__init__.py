__all__ = [
    'ClientView',
    'ClientCreateView',
    'ClientUpdateView',
    'ClientDeleteView',

    'MessageView',
    'MessageCreateView',
    'MessageUpdateView',
    'MessageDeleteView',
]

from app.mailings.views.client_view import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView
from app.mailings.views.message_view import MessageView, MessageCreateView, MessageUpdateView, MessageDeleteView
