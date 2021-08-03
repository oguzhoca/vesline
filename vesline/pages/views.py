from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . forms import ContactForm, IsForm, StajForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class KvkView(TemplateView):
    template_name = 'kvk.html'

class MisyonView(TemplateView):
    template_name = 'misyon.html'


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We received your request'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class IsbasvuruView(SuccessMessageMixin, FormView):
    template_name = 'isform.html'
    form_class = IsForm
    success_url = reverse_lazy('isform')
    success_message = 'Başvurunuzu Aldık'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StajView(SuccessMessageMixin, FormView):
    template_name = 'stajform.html'
    form_class = StajForm
    success_url = reverse_lazy('stajform')
    success_message = 'Başvurunuzu Aldık'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
