# -*- coding: utf-8 -*-
import scrapy
import unicodedata
from tfgObtencionDatos.items import Partido
import datetime

class PnfgBasicSpider(scrapy.Spider):
    name = 'pnfgBasic'
    fileName='./outputs/PNFGBasic_' + datetime.datetime.today().strftime('%y%m%d%H%M%S') + '.json'
    custom_settings = {
        'FEED_URI': fileName,
        'FEED_FORMAT': 'json',
        'FEED_EXPORTERS': {
            'json': 'scrapy.exporters.JsonItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
        'LOG_FILE': 'spiderLog/pnfgBasic.log',
    }
    def __init__(self, federacion=None, grupo=None, competicion=None, temporada=None, xornada=0,url=None,*args, **kwargs):
        super(PnfgBasicSpider, self).__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
            self.idXornada=xornada
        else:
            urlAux='pnfg/NPcd/NFG_VisCalendario_Vis?cod_primaria=1000120&codgrupo='+grupo+'&codcompeticion='+competicion+'&codtemporada=' + temporada + 'CodJornada=1&CDetalle=1'
            self.idXornada=xornada
            if(federacion=='arg'):
                self.start_urls = ['http://www.futbolaragon.com/%s' % urlAux]
            if(federacion=='mur'):
                self.start_urls = ['http://www.ffrm.es/%s' % urlAux]
            if(federacion=='ext'):
                self.start_urls = ['http://www.fexfutbol.com/%s' % urlAux]

    def parse(self, response):
        if(self.idXornada==0):
            path='//div[@id="trPartidosJornada_1"]'
            divXornada=response.xpath(path)
            j=1
            while divXornada!=[]:
                partidos=divXornada.xpath('./table/tr')
                for p in partidos[1:len(partidos)-1]:
                    tempo=str(p.xpath('./td[7]/span/text()').get() or '').split(' - ')
                    if len(tempo)>1:
                        dataAux=tempo[0]
                        horaAux=tempo[1]
                    else:
                        horaAux=''
                        dataAux=str(p.xpath('./td[7]/span/text()').get() or ' ')
                    partido= Partido(
                                local=str(p.xpath('./td[1]/text()').get().strip() or ' '),
                                visitante=str(p.xpath('./td[5]/text()').get().strip() or ' '),
                                ptsL=str(p.xpath('./td[2]/text()').get().strip() or ' '),
                                ptsV=str(p.xpath('./td[4]/text()').get().strip() or ' '),
                                localizacion=str(p.xpath('./td[6]/text()').get().strip() or ' '),
                                data=str(dataAux.strip() or ' '),
                                hora=str(horaAux.strip() or ' '),
                                xornada=j
                                )
                    yield partido
                j=j+1
                path='//div[@id="trPartidosJornada_%s"]' %j
                divXornada=response.xpath(path)
            pass
        else:
            path='//div[@id="trPartidosJornada_%s"]' % self.idXornada
            divXornada=response.xpath(path)
            partidos=divXornada.xpath('./table/tr')
            for p in partidos[1:len(partidos)-1]:
                tempo=str(p.xpath('./td[7]/span/text()').get() or '').split(' - ')
                if len(tempo)>1:
                    dataAux=tempo[0]
                    horaAux=tempo[1]
                else:
                    horaAux=''
                    dataAux=str(p.xpath('./td[7]/span/text()').get() or ' ')
                partido= Partido(
                            local=str(p.xpath('./td[1]/text()').get().strip() or ' '),
                            visitante=str(p.xpath('./td[5]/text()').get().strip() or ' '),
                            ptsL=str(p.xpath('./td[2]/text()').get().strip() or ' '),
                            ptsV=str(p.xpath('./td[4]/text()').get().strip() or ' '),
                            localizacion=str(p.xpath('./td[6]/text()').get().strip() or ' '),
                            data=str(dataAux.strip() or ' '),
                            hora=str(horaAux.strip() or ' '),
                            xornada=self.idXornada
                            )
                yield partido
        print(self.fileName)
    pass
