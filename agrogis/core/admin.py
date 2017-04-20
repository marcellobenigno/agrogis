from django.contrib.admin import AdminSite
from django.contrib.gis import admin
from django.forms.widgets import Textarea

from .models import *


class ProprietarioAdmin(admin.ModelAdmin):
    model = Proprietario
    list_display = ['nome', 'sobrenome', 'cpf']
    search_fields = ['nome', 'sobrenome', 'cpf']


admin.site.register(Proprietario, ProprietarioAdmin)


class ImovelRuralAdmin(admin.ModelAdmin):
    model = ImovelRural
    list_display = ['nome', 'cod_incra', 'certidao', 'dt_certif', 'proprietario']
    search_fields = ['nome']

    formfield_overrides = {
        models.MultiPolygonField: {'widget': Textarea}
    }


admin.site.register(ImovelRural, ImovelRuralAdmin)


class SafraAdmin(admin.ModelAdmin):
    model = Safra
    list_display = ['nome', 'geocodigo', 'ms_ucs']
    search_fields = ['ms_ucs']

    formfield_overrides = {
        models.MultiPolygonField: {'widget': Textarea}
    }


admin.site.register(Safra, SafraAdmin)


class MunicipioAdmin(admin.ModelAdmin):
    model = Municipio
    list_display = ['nome', 'meso', 'micro']
    search_fields = ['nome']

    formfield_overrides = {
        models.MultiPolygonField: {'widget': Textarea}
    }


admin.site.register(Municipio, MunicipioAdmin)


class MyAdminSite(AdminSite):
    AdminSite.site_header = "AgroGIS - Painel de Controle"
    AdminSite.index_title = "AgroGIS - Admininstração do Sistema"
