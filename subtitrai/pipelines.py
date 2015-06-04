# -*- coding: utf-8 -*-


class ItemCleanerPipeline(object):

    @staticmethod
    def fix_url(url):
        prefix = "../../"
        if url.startswith(prefix):
            url = url[len(prefix):]
        return "http://www.subtitrai.net/%s" % url

    def process_item(self, item, spider):
        item["file_urls"] = [
            ItemCleanerPipeline.fix_url(url) for url in item["file_urls"]
        ]
        return item
