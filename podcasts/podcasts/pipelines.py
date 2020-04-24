# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from scrapy.http import Request

class mp3FilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        print('-'*60)
        print(request.meta)
        print('-'*60)
        return request.meta['filename']
        
    def get_media_requests(self, item, info):
        file_url = item['file_urls'][0]
        print(file_url)
        meta = {'filename': item['files']}
        yield Request(url=file_url, meta=meta)

class PodcastsPipeline(object):
    def process_item(self, item, spider):
        return item
