from django.urls import path

from .views import index, oculto, oculto2

urlpatterns = [
    path('', index, name='index'),
    path('hidden', oculto, name='oculto'),
    path('acha-oculto-ctf', oculto2, name='oculto2')
]
    