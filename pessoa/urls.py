from django.urls import path
from .views import ListaPessoaView
from . import views


app_name = "pessoa"


urlpatterns = [
    path("pessoa/", views.pagepessoa, name="pagepessoa"),

]
