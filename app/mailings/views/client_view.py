from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from app.mailings.models import Client


class ClientView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailings:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'comment']
    success_url = reverse_lazy('mailings:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:client_list')

