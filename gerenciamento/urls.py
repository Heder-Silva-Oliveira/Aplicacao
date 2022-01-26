from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local
    path("", include("pages.urls", namespace="pages")),
    path("", include("pages.urls", namespace="storepage")),
    path("", include("pessoa.urls", namespace="pagepessoa")),

]
