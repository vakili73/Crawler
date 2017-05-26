# -*- coding: utf-8 -*-
import scrapy

class KhanehkheshtiSpider(scrapy.Spider):
    name = "khanehkheshti"
    allowed_domains = ["khanehkheshti.com"]
    start_urls = ['http://khanehkheshti.com/']

    def parse(self, response):
        categories = response.xpath("//*[@id='navigation']/ul/li/a/text()").extract()
        pass