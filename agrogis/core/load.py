import os

from django.contrib.gis.utils import LayerMapping

from .models import ImovelRural, Municipio, Safra

imovelrural_mapping = {
    'cod_incra': 'cod_incra',
    'nome': 'nome',
    'certidao': 'certidao',
    'dt_certif': 'dt_certif',
    'proprietario': 'prop_id',
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

# data_dir = os.path.abspath(os.path.join('core', 'data')) + '/'

lm1 = LayerMapping(ImovelRural, 'agrogis/core/data/imoveis_rurais.shp', imovelrural_mapping)
lm2 = LayerMapping(Municipio, 'agrogis/core/data/municipios.shp', municipio_mapping)
lm3 = LayerMapping(Safra, 'agrogis/core/data/safra_2016_verao.shp', safra_mapping)
