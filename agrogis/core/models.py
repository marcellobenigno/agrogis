from django.contrib.gis.db import models


class ImovelRural(models.Model):
    cod_incra = models.CharField('cód. do INCRA', max_length=254)
    nome = models.CharField('nome', max_length=254)
    certidao = models.CharField('certidão', max_length=254)
    dt_certif = models.CharField('data da certificação', max_length=254)
    proprietario = models.ForeignKey('Proprietario', verbose_name='proprietário')
    geom = models.MultiPolygonField('geom', srid=4326)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Imóvel Rural'
        verbose_name_plural = 'Imóveis Rurais'
        ordering = ['nome']


class Municipio(models.Model):
    nome = models.CharField('nome', max_length=50)
    meso = models.CharField('mesoregião', max_length=100)
    micro = models.CharField('microregião', max_length=100)
    geom = models.MultiPolygonField('geom', srid=4326)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Município'
        verbose_name_plural = 'Municípios'
        ordering = ['nome']


class Safra(models.Model):
    geocodigo = models.CharField('geocódigo', max_length=20)
    nome = models.CharField('nome', max_length=60)
    ms_ucs = models.CharField('cultura', max_length=12)
    geom = models.MultiPolygonField('geom', srid=4326)

    def __str__(self):
        return self.ms_ucs

    class Meta:
        verbose_name = 'Safra'
        verbose_name_plural = 'Safras'
        ordering = ['ms_ucs']


class Proprietario(models.Model):
    nome = models.CharField('nome', max_length=30)
    sobrenome = models.CharField('sobrenome', max_length=30)
    cpf = models.CharField('CPF', max_length=11, unique=True)

    def __str__(self):
        return "CPF: {}".format(self.cpf)

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'
        ordering = ['nome']

# class AreaPlantada(models.Model):
#     cultura = models.CharField('Culturas', max_length=255)
#     area_ha = models.DecimalField('área em hectares', max_digits=10, decimal_places=2)
#     imovel_rural = models.ForeignKey('ImovelRural', verbose_name='imóvel rural')
#     geom = models.MultiPolygonField('geom', srid=4326)
#
#     def __str__(self):
#         return self.imovel_rural
#
#     class Meta:
#         verbose_name = 'área plantada'
#         verbose_name_plural = 'áreas plantadas'
#         ordering = ['cultura']
