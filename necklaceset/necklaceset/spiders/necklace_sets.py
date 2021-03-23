import scrapy
import json
from scrapy.exporters import JsonItemExporter

class necklace(scrapy.Spider):
    name = "sets"
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat/']

    def parse(self, response):
        # Extract product information
        sub_url = response.css('li::attr(data-url)').extract()
        for h in range(0, len(sub_url)):
            url = sub_url[h]
            yield scrapy.Request(url, callback=self.parse)
        item = dict()
        item['title'] = "".join(response.xpath('/html/body/div[3]/div[4]/div/div[2]/div[2]/h1/text()').extract())
        item['description'] = "".join(response.css('#tab-1 ::text').extract())
        item['images'] = response.css('#productsections > ul ::attr(data-image)').extract()
        item['prices'] = "".join(response.xpath('/html/body/div[3]/div[4]/div/div[2]/div[2]/h4/span[2]/text()').extract())
        yield item





