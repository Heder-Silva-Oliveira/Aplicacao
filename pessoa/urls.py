from django.urls import path
from .views import ListaPessoaView
from . import views


app_name = "pessoa"


urlpatterns = [
    #path("pessoa/", views.pagepessoa, name="pagepessoa"),
    path("pessoa/", views.form_modelform, name="form_modelform"),

]
