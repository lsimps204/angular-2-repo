"""recipe_backend URL Configuration """

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/api/recipes')),
    path('admin/', admin.site.urls),
    path('api/recipes/', include('recipes_api.urls'))
]
