from django.views.generic import TemplateView
from django.shortcuts import render
from pessoa.models import Pessoa
from django.db.models import Count


def storepage(request):

    data = Pessoa.objects.all().values('uf').annotate(total=Count('uf')).order_by('uf')


    return render(request, 'store.html', context={'data': data})


class HomePageView(TemplateView):
    template_name = "home.html"



