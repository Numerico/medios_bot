from django.shortcuts import render
from models import Ubicacion

def mapa(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'medios_libres/mapa.html', {'ubicaciones': ubicaciones})
