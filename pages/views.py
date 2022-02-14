from django.views.generic import TemplateView
from django.shortcuts import render
from pessoa.models import Pessoa


def storepage(request):
    return render(request, 'store.html')


class HomePageView(TemplateView):
    template_name = "home.html"


