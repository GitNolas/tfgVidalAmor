# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Partido(scrapy.Item):
    local=scrapy.Field()
    visitante=scrapy.Field()
    ptsL=scrapy.Field()
    ptsV=scrapy.Field()
    xornada=scrapy.Field()
    localizacion=scrapy.Field()
    data=scrapy.Field()
    hora=scrapy.Field()
    pass
