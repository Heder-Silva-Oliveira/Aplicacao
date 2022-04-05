from django.shortcuts import render
from django.views.generic import ListView

from .forms import PessoaForm
from .models import Pessoa


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


def grafico(request):
    graf = Pessoa.uf.all().order_by('uf')
    context = {
        'graf': graf
    }
    return render(request, "store.html", context=context)