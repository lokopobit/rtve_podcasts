# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:10:26 2020

@author: lokopobit
"""

import os
import scrapy

class mp3filesItem(scrapy.Item):
     file_urls = scrapy.Field()
     files = scrapy.Field()

class mp3_spider(scrapy.Spider):
    name = "mp3files"

    def start_requests(self):
        self.urls = ['https://www.rtve.es/alacarta/audios/discopolis/']
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.find_contenttable)

    def find_contenttable(self, response):
        all_urls = response.selector.xpath('//a/@href').extract()
        contenttable_urls = [u for u in all_urls if u.find('modl=TOC') != -1]
        first_contentable_url = contenttable_urls[0]
        page_numbers = [u[u.find('pbq=')+4:u.find('&')] for u in contenttable_urls]
        page_numbers = [int(n) for n in page_numbers]
        urls_table = []
        for n in range(1,max(page_numbers)+1):
            urls_table.append(first_contentable_url.replace('pbq=1','pbq='+str(n)))
            
        for url_table in urls_table[:1]:
            yield scrapy.Request(url='https://www.rtve.es'+url_table, callback=self.parse_contenttable)
            
    def parse_contenttable(self, response):
        all_urls = response.selector.xpath('//a/@href').extract()
        b = [a for a in all_urls if a.find('discopolis') != -1]
        c = [b[i].split('/')[-3] for i in list(range(0,len(b),2))]
        print('*'*60)
        print(c[:4])
        print('*'*60)
        mp3_urls = [url for url in all_urls if url[-3:] == 'mp3']
        mp3_dates = response.selector.xpath('//span[@class="col_fec"]/text()').getall()
        mp3_dates = [mp3d.replace(' ','') for mp3d in mp3_dates]
        for mp3_url in mp3_urls[:1]:
            item = mp3filesItem()
            item['file_urls'] = [mp3_url]
            path = self.urls[0][self.urls[0].find('audios/')+len('audios/'):-1]
            filename = mp3_dates[mp3_urls.index(mp3_url)]+'.mp3'
            item['files'] = os.path.join(path, filename)
            yield item