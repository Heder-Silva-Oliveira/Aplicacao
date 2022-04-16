import json

from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView
import conectdb

from .forms import PessoaForm
from pessoa.models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')


# def pagepessoa(request):
#     return render(request, 'pessoa.html')


def form_modelform(request):
    if request.method == "GET":
        form = PessoaForm()
        context = {
            'form': form
        }
        return render(request, "pessoa.html", context=context)
    else:
        form = PessoaForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = PessoaForm()
        context = {
            'form': form
        }
        return render(request, "pessoa.html", context=context)


def clientes(request):
    data = {Pessoa.objects.all().values('us').annotate(total=Count('uf')).order_by('-total')}
    return render(request, "home.html", context={'data': data})






