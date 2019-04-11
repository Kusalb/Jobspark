# -*- coding: utf-8 -*-
import scrapy
from ..items import MerojobItem


class KantipurjobSpider(scrapy.Spider):
    name = 'kantipurjob'
    start_urls = ['https://kantipurjob.com']

    def parse(self, response):
        items = MerojobItem()
        kaj_company = response.css('.job-search-desc-blk a').css('::text').extract()
        kaj_job_title = response.css('.job-search-desc-blk span::text').extract()
        kaj_deadline = response.css('.col-md-3.right::text').extract()
        items['kaj_company'] = kaj_company
        items['kaj_job_title'] = kaj_job_title
        items['kaj_deadline'] = kaj_deadline
        yield items
