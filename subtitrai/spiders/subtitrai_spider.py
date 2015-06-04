# -*- coding: utf-8 -*-
import scrapy

from subtitrai.items import SubtitraiItem


class SubtitraiSpider(scrapy.Spider):
    name = "subtitrai"
    allowed_domains = ["subtitrai.net"]
    start_urls = [
        "http://www.subtitrai.net/subtitrai.html",
    ]

    def parse(self, response):
        for sel in response.xpath("//div[@class='list']"):
            item = SubtitraiItem()
            title = sel.xpath("a/text()").extract()
            title = "".join(t.strip() for t in title)
            item["title"] = title
            item["url"] = sel.xpath("a/@href").extract()[0]
            request = scrapy.Request(
                "http://www.subtitrai.net/%s" % item["url"],
                callback=self.parse_subtitle_page
            )
            request.meta["item"] = item
            yield request

    def parse_subtitle_page(self, response):
        item = response.meta["item"]
        item["imdb_url"] = response.xpath(
            "//div[@id='imdb']/a/@href").extract()

        file_urls = []
        file_urls.extend(response.xpath(
            "//div[@class='ttdown']/a/@href").extract())
        file_urls.extend(response.xpath(
            "//div[@class='tt-white-d']/a/@href").extract())
        item["file_urls"] = file_urls

        yield item
