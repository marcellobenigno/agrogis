import os

from django.contrib.gis.utils import LayerMapping

from .models import ImovelRural, Municipio, Safra

imovelrural_mapping = {
    'cod_incra': 'cod_incra',
    'nome': 'nome',
    'certidao': 'certidao',
    'dt_certif': 'dt_certif',
    'prop_id': 'prop_id',
    'geom': 'MULTIPOLYGON',
}

municipio_mapping = {
    'nome': 'nome',
    'meso': 'meso',
    'micro': 'micro',
    'geom': 'MULTIPOLYGON',
}

safra_mapping = {
    'geocodigo': 'geocodigo',
    'nome': 'nome',
    'ms_ucs': 'ms_ucs',
    'geom': 'MULTIPOLYGON',
}

data_dir = os.path.abspath(os.path.join('core', 'data')) + '/'

lm1 = LayerMapping(ImovelRural, data_dir + 'imoveis_rurais.shp', imovelrural_mapping)
lm2 = LayerMapping(Municipio, data_dir + 'municipios.shp', municipio_mapping)
lm3 = LayerMapping(Safra, data_dir + 'safra_2016_verao.shp', safra_mapping)
