# -*- coding: utf-8 -*-

# Scrapy settings for subtitrai project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'subtitrai'

SPIDER_MODULES = ['subtitrai.spiders']
NEWSPIDER_MODULE = 'subtitrai.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'subtitrai (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'subtitrai.pipelines.ItemCleanerPipeline': 300,
    'scrapy.contrib.pipeline.files.FilesPipeline': 400,
}

# Directory to store the downloaded files in (create it beforehand)
FILES_STORE = './subtitles'
