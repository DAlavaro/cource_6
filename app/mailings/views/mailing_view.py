from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from app.mailings.models import Mailing, Client
from django import forms
from django.shortcuts import get_object_or_404
from django.core.mail import send_mass_mail
from django.http import HttpResponseRedirect
from django.views import View
from config.settings import EMAIL_HOST_USER


class MailingForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))
    end_time = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))
    client = forms.ModelMultipleChoiceField(queryset=Client.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Mailing
        fields = ['name', 'start_time', 'end_time', 'periodicity', 'status', 'client', 'message']


class MailingView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.save()
        form.save_m2m()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')


class MailingSendView(View):

    def get(self, request, *args, **kwargs):
        mailing = get_object_or_404(Mailing, pk=kwargs['pk'])
        messages = [(mailing.name, mailing.message.message, EMAIL_HOST_USER, [client.email]) for client in
                    mailing.client.all()]

        send_mass_mail(messages)

        return HttpResponseRedirect(reverse('mailings:mailing_list'))
