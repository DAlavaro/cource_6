from django.urls import path
from app.mailings.views import ClientView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = 'mailings'


urlpatterns = [
    path('client/', ClientView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
