# -*- coding: utf-8 -*-
import scrapy
import unicodedata
from tfgObtencionDatos.items import Partido
import datetime
class PnfgSpider(scrapy.Spider):
    name = 'pnfg'
    fileName='./outputs/PNFG_' + datetime.datetime.today().strftime('%y%m%d%H%M%S') + '.json'
    custom_settings = {
        'FEED_URI': fileName,
        'FEED_FORMAT': 'json',
        'FEED_EXPORTERS': {
            'json': 'scrapy.exporters.JsonItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
        'LOG_FILE': 'spiderLog/pnfg.log',
    }
    def __init__(self, federacion=None, grupo=None, competicion=None, temporada=None, xornada=0,url=None,*args, **kwargs):

        super(PnfgSpider, self).__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
            self.idXornada=xornada
        else:
            urlAux='pnfg/NPcd/NFG_VisCalendario_Vis?cod_primaria=1000120&codgrupo='+grupo+'&codcompeticion='+competicion+'&codtemporada=' + temporada + 'CodJornada=1&CDetalle=1'
            self.idXornada=xornada
            if(federacion=='gal'):
                self.start_urls = ['http://www.futgal.es/%s' % urlAux]
            if(federacion=='mad'):
                self.start_urls = ['https://www.rffm.es/%s' % urlAux]
            if(federacion=='ceu'):
                self.start_urls = ['http://www.ffce.es/%s' % urlAux]
            if(federacion=='rioj'):
                self.start_urls = ['https://www.frfutbol.com/%s' % urlAux]
            if(federacion=='clm'):
                self.start_urls = ['https://www.ffcm.es/%s' % urlAux]
            if(federacion=='and'):
                self.start_urls = ['http://www.faf.es/%s' % urlAux]
            if(federacion=='cant'):
                self.start_urls = ['https://www.federacioncantabradefutbol.com/%s' % urlAux]
    def parse(self, response):
        xornadas=response.xpath('//table[@class="table table-striped table-hover"]')
        if self.idXornada==0:
            first=0
            last=len(xornadas)
        else:
            first=int(self.idXornada)-1
            last=int(self.idXornada)
        for j in range(first, last, 1):
            partidos=xornadas[j].xpath('./tr/td/div[1]')
            partidosInfo=xornadas[j].xpath('./tr/td/div[2]')
            for i in range(len(partidos)):
                tempo=unicodedata.normalize("NFKD", partidosInfo[i].xpath('./text()').getall()[3]).split(' - ')
                if len(tempo)>1:
                    dataAux=tempo[0]
                    horaAux=tempo[1]
                else:
                    d=partidosInfo[i].xpath('./text()').getall()
                    dataAux=partidosInfo[i].xpath('./text()').getall()[len(d)-1]
                    horaAux=''
                partido= Partido(
                                local=unicodedata.normalize("NFKD", str(partidos[i].xpath('./table/tr/td[1]/strong/span/text()').get() or 'Descansa')).strip(),
                                visitante=unicodedata.normalize("NFKD", str(partidos[i].xpath('./table/tr/td[3]/strong/span/text()').get() or 'Descansa')).strip(),
                                ptsL=unicodedata.normalize("NFKD", str(partidos[i].xpath('./table/tr/td[2]/text()').getall()[0]) or '').strip(),
                                ptsV=unicodedata.normalize("NFKD", str(partidos[i].xpath('./table/tr/td[2]/text()').getall()[1]) or '').strip(),
                                localizacion=unicodedata.normalize("NFKD", str(partidosInfo[i].xpath('./text()').getall()[1]) or '').strip(),
                                data=unicodedata.normalize("NFKD", dataAux).strip(),
                                hora=unicodedata.normalize("NFKD", horaAux).strip(),
                                xornada=j+1
                                )
                yield(partido)
        print(self.fileName)
        pass
