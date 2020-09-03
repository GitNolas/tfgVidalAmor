# -*- coding: utf-8 -*-
import scrapy
import unicodedata
from tfgObtencionDatos.items import Partido
import datetime

class BalonmanSpider(scrapy.Spider):
    name = 'balonman'
    fileName='./outputs/Balonman_' + datetime.datetime.today().strftime('%y%m%d%H%M%S') + '.json'
    custom_settings = {
        'FEED_URI': fileName,
        'FEED_FORMAT': 'json',
        'FEED_EXPORTERS': {
            'json': 'scrapy.exporters.JsonItemExporter',
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
        'LOG_FILE': 'spiderLog/balonman.log',
    }
    def __init__(self, competicion=None, xornada=0, url=None, *args, **kwargs):
        super(BalonmanSpider, self).__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
            self.idXornada=xornada
        else:
            self.idXornada=xornada
            if (xornada==0 ):
                self.start_urls = ['https://www.rfebm.com/competiciones/calendario.php?seleccion=0&id=%s&id_ambito=0' % competicion]
            else:
                self.start_urls = ['https://www.rfebm.com/competiciones/competicion.php?seleccion=0&id=%s&jornada=%s&id_ambito=0' % (competicion, xornada)]


    def parse(self, response):
        partidos=response.xpath('//table[@class="table table-striped"]/tbody/tr')
        for p in partidos:
            if p.xpath('./td[3]/a[1]/text()')==[] :
                self.idXornada=self.idXornada +1
                continue
            partido= Partido(
                            local=str(p.xpath('./td[3]/a[1]/text()').get() or '').strip(),
                            visitante=str(p.xpath('./td[3]/a[2]/text()').get() or '').strip(),
                            ptsL=str(p.xpath('./td[4]/span[1]/text()').get() or '').strip(),
                            ptsV=str(p.xpath('./td[4]/span[2]/text()').get() or '').strip(),
                            data=str(p.xpath('./td[5]/div[1]/text()').get() or '').strip(),
                            hora=str(p.xpath('./td[5]/div[2]/text()').get() or '').strip(),
                            localizacion=str(p.xpath('./td[6]/a/text()').get() or '').strip(),
                            xornada=self.idXornada
                            )
            yield(partido)
        print(self.fileName)
        pass
