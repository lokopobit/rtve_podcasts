# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:10:26 2020

@author: lokopobit
"""

import scrapy
from scrapy.pipelines.files import FilesPipeline

class MyFilesPipeline(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        return 'files/' + 'amostu.mp3'
    


class mp3filesItem(scrapy.Item):
     file_urls = scrapy.Field()
     files = scrapy.Field()
     path = scrapy.Field()

class mp3_spider(scrapy.Spider):
    name = "mp3files"

    def start_requests(self):
        urls = ['https://www.rtve.es/alacarta/audios/discopolis/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_contenttable)

    def parse_contenttable(self, response):
        all_urls = response.selector.xpath('//a/@href').extract()
        contenttable_urls = [u for u in all_urls if u.find('modl=TOC') != -1]
        first_contentable_url = contenttable_urls[0]
        page_numbers = [u[u.find('pbq=')+4:u.find('&')] for u in contenttable_urls]
        page_numbers = [int(n) for n in page_numbers]
        urls_table = []
        for n in range(1,max(page_numbers)+1):
            urls_table.append(first_contentable_url.replace('pbq=1','pbq='+str(n)))
            
        for url_table in urls_table[:1]:
            yield scrapy.Request(url='https://www.rtve.es'+url_table, callback=self.parse_mp3)
            
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
        item['path'] = 'amostu/as.mp3'
        yield item