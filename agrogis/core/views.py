from django.shortcuts import render

from .models import ImovelRural, Municipio, Safra


def home(request):
    return render(request, 'index.html')


def webgis(request):
    return render(request, 'webgis.html')


def search(request):
    imoveis_rurais = ImovelRural.objects.all()[0:10]
    areas_plantadas = Safra.objects.all()
    plantacoes = []
    for imovel_rural in imoveis_rurais:
        item = {'id': imovel_rural.id, 'culturas': []}
        for area_plantada in areas_plantadas:
            if imovel_rural.geom.intersects(area_plantada.geom):
                if not area_plantada.ms_ucs in item['culturas']:
                    item['culturas'].append(area_plantada.ms_ucs)
        plantacoes.append(item)

    context = {
        'imoveis_rurais': imoveis_rurais,
        'plantacoes': plantacoes
    }

    return render(request, 'search.html', context)


def detail(request, pk):
    imovel_rural = ImovelRural.objects.get(pk=pk)
    municipio = Municipio.objects.get(geom__contains=imovel_rural.geom.centroid)
    area_ha = get_area_ha(pk)
    areas_plantadas = Safra.objects.filter(geom__intersects=imovel_rural.geom)
    plantacoes = []
    for area in areas_plantadas:
        if not area.ms_ucs in plantacoes:
            plantacoes.append(area.ms_ucs)

    context = {
        'imovel_rural': imovel_rural,
        'municipio': municipio,
        'area_ha': area_ha,
        'plantacoes': plantacoes,
    }
    return render(request, 'detail.html', context)


def get_area_ha(pk):
    sql = """SELECT id, ST_Area(geom :: GEOGRAPHY)/10000 AS area_ha FROM core_imovelrural WHERE id = {}""".format(pk)
    result = ImovelRural.objects.raw(sql)
    return result[0].area_ha
