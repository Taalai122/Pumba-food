from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# Create your views here

class IndexView(TemplateView):
    template_name = 'pages/index_home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html' # Переменная для приема шаблонов

    def get_context_data(self, **kwargs):# метод для стягивания данных из базы в шаблон
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        context['employees'] = Employees.objects.all()
        return context