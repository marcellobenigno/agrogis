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
    area_ha = get_area_ha(pk)
    context = {
        'imovel_rural': imovel_rural,
        'municipio': municipio,
        'area_ha': area_ha
    }
    return render(request, 'detail.html', context)


def get_area_ha(pk):
    sql = """SELECT id, ST_Area(geom :: GEOGRAPHY)/10000 AS area_ha FROM core_imovelrural WHERE id = {}""".format(pk)
    result = ImovelRural.objects.raw(sql)
    return result[0].area_ha
