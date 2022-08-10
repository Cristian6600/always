from venv import create
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import HttpResponse
from . models import Contacto

class QHola(TemplateView):
    template_name = "home/index.html"

class ContatoCreateView(CreateView):
    template_name = "home/contacto.html"
    model = Contacto
    fields = "__all__"
    success_url = '.'
