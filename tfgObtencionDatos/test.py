import unittest
import os
import json
import requests
from tfgObtencionDatos.spiders import pnfg
from tfgObtencionDatos.spiders import pnfgBasic
from tfgObtencionDatos.spiders import balonman
from response import fake_response_from_file
class PnfgSpiderTest(unittest.TestCase):

    def setUp(self):
        self.path='../HTMLTests/PNFG/'
        self.spider = pnfg.PnfgSpider(url='a')
        self.directorios=next(os.walk(self.path))[1]

    def _test_item_results(self, results, directorio):
        with open('%s%s/data.json' %(self.path,directorio)) as f:
            data = json.load(f)
        #self.assertEqual(len(data), len(results))
        i= 0
        permalinks = set()
        for r in results:
            self.assertEqual(r['local'], data[i]['local'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['visitante'], data[i]['visitante'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['ptsL'], data[i]['ptsL'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['ptsV'], data[i]['ptsV'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['xornada'], data[i]['xornada'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['localizacion'], data[i]['localizacion'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['data'], data[i]['data'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['hora'], data[i]['hora'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            i+=1

    def test_parse(self):
        for d in self.directorios:
            results = self.spider.parse(fake_response_from_file('%s%s/index.html' %(self.path,d)))
            self._test_item_results(results, d)
        self.spider = pnfg.PnfgSpider(url='a')


class PnfgBasicSpiderTest(unittest.TestCase):

    def setUp(self):
        self.path='../HTMLTests/PNFGBasic/'
        self.spider = pnfgBasic.PnfgBasicSpider(url='a')
        self.directorios=next(os.walk(self.path))[1]

    def _test_item_results(self, results, directorio):
        with open('%s%s/data.json' %(self.path,directorio)) as f:
            data = json.load(f)
        #self.assertEqual(len(data), len(results))
        i= 0
        permalinks = set()
        for r in results:
            self.assertEqual(r['local'], data[i]['local'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['visitante'], data[i]['visitante'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['ptsL'], data[i]['ptsL'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['ptsV'], data[i]['ptsV'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['xornada'], data[i]['xornada'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['localizacion'], data[i]['localizacion'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['data'], data[i]['data'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['hora'], data[i]['hora'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            i+=1

    def test_parse(self):
        for d in self.directorios:
            results = self.spider.parse(fake_response_from_file('%s%s/index.html' %(self.path,d)))
            self._test_item_results(results, d)
        self.spider = pnfgBasic.PnfgBasicSpider(url='a')

class BalonmanSpiderTest(unittest.TestCase):

    def setUp(self):
        self.path='../HTMLTests/Balonman/'
        self.spider = balonman.BalonmanSpider(url='a', xornada=0)
        self.directorios=next(os.walk(self.path))[1]

    def _test_item_results(self, results, directorio):
        filePath='%s%s/data.json' %(self.path,directorio)
        with open(filePath) as f:
            data = json.load(f)
        #self.assertEqual(len(data), len(results))
        i= 0
        permalinks = set()
        for r in results:
            self.assertEqual(r['local'], data[i]['local'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['visitante'], data[i]['visitante'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['ptsL'], data[i]['ptsL'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['ptsV'], data[i]['ptsV'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['xornada'], data[i]['xornada'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['localizacion'], data[i]['localizacion'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['data'], data[i]['data'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            self.assertEqual(r['hora'], data[i]['hora'], msg='\n--> FILE: %s \n--> LINE:%s \n' %(directorio,i))
            i+=1

    def test_parse(self):
        for d in self.directorios:
            results = self.spider.parse(fake_response_from_file('%s%s/index.html' %(self.path,d)))
            self._test_item_results(results, d)
            self.spider = balonman.BalonmanSpider(url='a', xornada=0)

class PnfgURLTest(unittest.TestCase):
    def setUp(self):
        self.file='../HTMLTests/PNFG/url.json'
        with open(self.file) as f:
            self.data = json.load(f)
        self.spider = pnfg.PnfgSpider(url='a')

    def test_parse(self):
        for url in self.data:
            self.spider = pnfg.PnfgSpider(
                                            federacion=url['idFederacion'],
                                            competicion=url['idCompeticion'],
                                            grupo=url['idGrupo'],
                                            temporada=url['idTemporada'],)
            r=requests.get(self.spider.start_urls[0]).text
            self.assertNotEqual(len(r),0, msg='\n--> URL:%s\n-->JSON Federacion:%s\n-->JSON Competicion:%s\n-->JSON Grupo:%s'
                                                % (self.spider.start_urls[0],url['idFederacion'],url['idCompeticion'],url['idGrupo']))


class PnfgBasicURLTest(unittest.TestCase):
    def setUp(self):
        self.file='../HTMLTests/PNFGBasic/url.json'
        with open(self.file) as f:
            self.data = json.load(f)
        self.spider = pnfgBasic.PnfgBasicSpider(url='a')

    def test_parse(self):
        for url in self.data:
            self.spider = pnfgBasic.PnfgBasicSpider(
                                            federacion=url['idFederacion'],
                                            competicion=url['idCompeticion'],
                                            grupo=url['idGrupo'],
                                            temporada=url['idTemporada'],)
            r=requests.get(self.spider.start_urls[0]).text
            self.assertNotEqual(len(r),0, msg='\n--> URL:%s\n-->JSON Federacion:%s\n-->JSON Competicion:%s\n-->JSON Grupo:%s'
                                                % (self.spider.start_urls[0],url['idFederacion'],url['idCompeticion'],url['idGrupo']))


class BalonmanURLTest(unittest.TestCase):
    def setUp(self):
        self.file='../HTMLTests/Balonman/url.json'
        with open(self.file) as f:
            self.data = json.load(f)
        self.spider = balonman.BalonmanSpider(url='a')

    def test_parse(self):
        for url in self.data:
            self.spider =balonman.BalonmanSpider(competicion=url['idCompeticion'])
            r=requests.get(self.spider.start_urls[0]).text
            self.assertGreater(len(r),2000, msg='\n--> URL:%s\n-->JSON Competicion:%s'
                                                % (self.spider.start_urls[0],url['idCompeticion']))
