# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from hinative.items import HinativeItem


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["hinative.com"]
    user_range = range(639970,689970)
    start_urls = ['https://hinative.com/en-US/profiles/'+str(i) for i in user_range]
    
    def compact(self, s):
        return s if s else None

    def parse(self, response):
        """
        item = HinativeItem()
        item['username'] = response.xpath(
            '//h1[@class="owner_name"]/span/text()').extract()[0].strip()
        """
        l = ItemLoader(item=HinativeItem(), response=response)
        l.add_xpath('a_username', '//*[@class="owner_name"]/span/text()',
                MapCompose(str.strip))

        l.add_xpath('b_natives','//*[@class="introduction_details language_native_table"]/p[@class="lang_parts"]/text()',
                MapCompose(str.strip, self.compact))

        l.add_xpath('c_learning','//*[@class="introduction_details language_study_table"]/a/span/text()',
                MapCompose(str.strip))

        return l.load_item()
