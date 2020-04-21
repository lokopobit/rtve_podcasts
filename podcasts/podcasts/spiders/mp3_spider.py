# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:10:26 2020

@author: lokopobit
"""

import scrapy

class mp3filesItem(scrapy.Item):
     file_urls = scrapy.Field()
     files = scrapy.Field()

class mp3_spider(scrapy.Spider):
    name = "mp3files"

    def start_requests(self):
        urls = ['https://www.rtve.es/alacarta/interno/contenttable.shtml?pbq=1&orderCriteria=DESC&modl=TOC&locale=es&pageSize=15&ctx=58212&advSearchOpen=false']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_mp3)

    def parse_mp3(self, response):
        all_urls = response.selector.xpath('//a/@href').extract()
        mp3_urls = [url for url in all_urls if url[-3:] == 'mp3']
        mp3_dates = response.selector.xpath('//span[@class="col_fec"]/text()').getall()
        print('*'*60)
        print(len(mp3_urls))
        print('*'*60)
        print(len(mp3_dates))
        print('*'*60)
        file_url = 'https://mediavod-lvlt.rtve.es/resources/TE_SSALTAM/mp3/0/1/1587396441710.mp3'
        item = mp3filesItem()
        item['file_urls'] = [file_url]
        yield item