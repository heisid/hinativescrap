# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HinativeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # Yes I'm using weird a,b,c in field names
    # Somehow scrapy orders the fields in alphabetical order in result
    a_username = scrapy.Field()
    b_natives = scrapy.Field()
    c_learning = scrapy.Field()
