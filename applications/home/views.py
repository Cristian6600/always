from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
import datetime

class QHola(TemplateView):
    template_name = "home/index.html"
