import scrapy
import sys
import os
import argparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

parser = argparse.ArgumentParser()
#Argumentos do Script
parser.add_argument('-f','--futbol', action='store_true')
parser.add_argument('-bm','--balonman', action='store_true')
parser.add_argument('-cF','--codigoFederacion', default='none')
parser.add_argument('-cC','--codigoCompeticion', required=True)
parser.add_argument('-cG','--codigoGrupo', default=None)
parser.add_argument('-cT','--codigoTemporada', default='15')
parser.add_argument('-cX','--codigoXornada', default=0)


args=parser.parse_args()
process = CrawlerProcess({'SPIDER_MODULES': 'tfgObtencionDatos.spiders'})
if args.futbol: #En caso de que se necesiten datos do Futbol
    federacionsPNFG=['gal', 'mad', 'ceu', 'rioj', 'clm', 'and', 'cant']
    federacionsPNFGBasic=['arg', 'mur', 'ext']
    if args.codigoFederacion in federacionsPNFG: #Scraper PNFG
        process.crawl(  'pnfg',
                        federacion=args.codigoFederacion,
                        grupo=args.codigoGrupo,
                        competicion=args.codigoCompeticion,
                        temporada=args.codigoTemporada,
                        xornada=args.codigoXornada)
        process.start()
    elif args.codigoFederacion in federacionsPNFGBasic: #Scraper PNFG basic
        process.crawl(  'pnfgBasic',
                        federacion=args.codigoFederacion,
                        grupo=args.codigoGrupo,
                        competicion=args.codigoCompeticion,
                        temporada=args.codigoTemporada,
                        xornada=args.codigoXornada
                     )
        process.start()
    else:
        print('Federación non existente')


if args.balonman: #Extraccion de datos para o Balonman
    process.crawl(  'balonman', #Scraper federacion espanola de balonman
                    competicion=args.codigoCompeticion,
                    xornada=args.codigoXornada
                 )
    process.start()
