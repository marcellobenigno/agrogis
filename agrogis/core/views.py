from django.shortcuts import render

from .models import ImovelRural, Municipio, Safra


def home(request):
    return render(request, 'index.html')


def webgis(request):
    return render(request, 'webgis.html')


def search(request):
    imoveis_rurais = ImovelRural.objects.all()
    areas_plantadas = Safra.objects.all()
    context = {
        'imoveis_rurais': imoveis_rurais,
        'areas_plantadas': areas_plantadas
    }

    return render(request, 'search.html', context)


def detail(request, pk):
    imovel_rural = ImovelRural.objects.get(pk=pk)
    municipio = Municipio.objects.get(geom__contains=imovel_rural.geom.centroid)

    context = {
        'imovel_rural': imovel_rural,
        'municipio': municipio,
    }
    return render(request, 'detail.html', context)
