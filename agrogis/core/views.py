from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render

from .util.pagination_helper import my_pagination, my_range, total_search_itens

from .models import ImovelRural, Municipio, Safra
from .forms import SearchForm


def home(request):
    return render(request, 'index.html')


def webgis(request):
    return render(request, 'webgis.html')


def search(request):
    form = SearchForm()
    imoveis_rurais = ImovelRural.objects.all()
    page = request.GET.get('page')

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            itens = form.cleaned_data
            imoveis_rurais = ImovelRural.objects.filter(
                nome__icontains=itens['nome'],
                proprietario__nome__icontains=itens['proprietario'],
                proprietario__cpf__icontains=itens['cpf']
            )

    result = imoveis_rurais.count()
    page_objects = my_pagination(imoveis_rurais, page)
    page_range = my_range(page_objects)

    selection = total_search_itens(itens)

    context = {
        'page_objects': page_objects,
        'page_range': page_range,
        'result': result,
        'selection': selection,
        'form': form,
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


def search_lnglat(request, lng, lat):
    point = GEOSGeometry('POINT({} {})'.format(lng, lat))
    imovel_rural = ImovelRural.objects.filter(geom__contains=point).first()

    context = {
        'imovel_rural': imovel_rural,
    }

    return render(request, 'search_lnglat.html', context)


def get_area_ha(pk):
    sql = """SELECT id, ST_Area(geom :: GEOGRAPHY)/10000 AS area_ha FROM core_imovelrural WHERE id = {}""".format(pk)
    result = ImovelRural.objects.raw(sql)
    return result[0].area_ha
