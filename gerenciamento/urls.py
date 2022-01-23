from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local
    path("", include("pages.urls", namespace="pages")),
    path("store/", include("pages.urls", namespace="storepage")),
    path("pessoa/", include("pessoa.urls", namespace="pessoapage")),

]
