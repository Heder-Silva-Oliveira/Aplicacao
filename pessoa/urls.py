from django.urls import path
from .views import ListaPessoaView
from . import views


app_name = "pessoa"


urlpatterns = [
    path('pessoa/', ListaPessoaView.as_view(), name='pessoa.index'),
    path('pessoa/', views.pessoapage, name='pessoapage'),
]
