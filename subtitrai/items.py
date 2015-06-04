# -*- coding: utf-8 -*-

import scrapy


class SubtitraiItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    imdb_url = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
