from scrapy.spider import Spider
from scrapy.selector import Selector
from itertools import izip
import csv

class APCSpider(Spider):
    name = "apc"
    allowed_domains = ["airnav.com"]
    start_urls = [
        "http://airnav.com/airports/us/CA",
        "http://airnav.com/airports/us/NY"
    ]

    def parse(self, response):
        sel = Selector(response)
        airport_ids = sel.xpath('/html/body/center/table//tr/td/a/text()').extract()
        airport_city = sel.xpath('/html/body/center/table//tr/td[3]/text()').extract()
        airport_name = sel.xpath('/html/body/center/table//tr/td[5]/text()').extract()
        with open('airports.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(izip(airport_ids,airport_name,airport_city))
