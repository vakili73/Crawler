# -*- coding: utf-8 -*-
import scrapy

class KhanehkheshtiSpider(scrapy.Spider):
    name = "khanehkheshti"
    allowed_domains = ["khanehkheshti.com"]
    start_urls = ['http://khanehkheshti.com/']

    def parse(self, response):
        categories = response.xpath("//*[@id='navigation']/ul/li/a").extract()
        f=open('file.txt', 'w', encoding='utf-8')
        for category in categories:
            f.write(category + '\n')
        f.close()
        pass