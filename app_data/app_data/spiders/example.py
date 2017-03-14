# -*- coding: utf-8 -*-
import scrapy

'''
class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass

import scrapy
'''

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
       	'''
        urls = [
        	'http://gaokao.chsi.com.cn/sch/search--ss-on,searchType-1,option-qg,start-0.dhtml',
            'http://gaokao.chsi.com.cn/sch/schoolInfo--schId-1,categoryId-26172,mindex-1.dhtml',
        ]
        '''
        urls = []
        for i in range(1,3):  #1,2
            urls.append('http://gaokao.chsi.com.cn/sch/schoolInfoMain--schId-'+str(i)+'.dhtml')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath("//div[@class='topImg']/text()").extract()
        sname = title[0]
        items = []
        for sit in response.xpath("//ul[@class='topNav clearfix']/li"):
            info = sit.xpath('a/text()').extract()
            href = sit.xpath('a/@href').extract()
            item = {} 
            item["herf"] = 'http://gaokao.chsi.com.cn' + href[0] 
            item["info"] = info[0]

            items.append(item)
        print("items=======",items)
        #msgTitle = title.extract()
        


