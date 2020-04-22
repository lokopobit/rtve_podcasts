# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline

class mp3FilesPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return 'files/' + 'amostu.mp3'

class PodcastsPipeline(object):
    def process_item(self, item, spider):
        return item
