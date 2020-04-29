# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 20:10:26 2020

@author: lokopobit
"""

import os
import scrapy
import pandas as pd
from scrapy.utils.project import get_project_settings

class mp3filesItem(scrapy.Item):
     file_urls = scrapy.Field()
     files = scrapy.Field()

class mp3_spider(scrapy.Spider):
    name = "mp3files"

    def start_requests(self):
        # 'https://www.rtve.es/alacarta/audios/discopolis/'  
        self.settings = get_project_settings()
        self.path = self.settings.get('FILES_STORE')
        self.urls = ['https://www.rtve.es/alacarta/audios/cuando-los-elefantes-suenan-con-la-musica/']
        self.name = self.urls[0].split('/')[-2]
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
            
        for url_table in list(reversed(urls_table))[:-1]: # [:10] 
            yield scrapy.Request(url='https://www.rtve.es'+url_table, callback=self.parse_contenttable)
            
    def parse_contenttable(self, response):
        all_urls = response.selector.xpath('//a/@href').extract()
        show_name = [a for a in all_urls if a.find(self.name) != -1]
        show_names = [show_name[i].split('/')[-3] for i in list(range(0,len(show_name),2))]
        mp3_urls = [url for url in all_urls if url[-3:] == 'mp3']
        mp3_dates = response.selector.xpath('//span[@class="col_fec"]/text()').getall()
        mp3_dates = [d.split(' ')[-1]+d.split(' ')[1]+d.split(' ')[0] for d in mp3_dates]
        #mp3_dates = [mp3d.replace(' ','') for mp3d in mp3_dates]
        
        if not os.path.exists(os.path.join(self.path, self.name)):
            os.mkdir(os.path.join(self.path, self.name))
        
        info_dict = dict(zip(mp3_dates, show_names)) 
        info_df = pd.DataFrame.from_dict(info_dict, orient='index', columns = ['name'])
        info_df.to_csv(os.path.join(self.path, self.name, mp3_dates[0])+'.csv')
        for mp3_url in mp3_urls:
            item = mp3filesItem()
            item['file_urls'] = [mp3_url]
            filename = mp3_dates[mp3_urls.index(mp3_url)]+'.mp3'
            
            # Check if mp3_url have already been downloaded
            downloaded_files = os.listdir(os.path.join(self.path, self.name))
            downloaded_files = [df for df in downloaded_files if df[-3:] == 'mp3']
            if filename in downloaded_files:
                continue
            
            item['files'] = os.path.join(self.name, filename)
            yield item