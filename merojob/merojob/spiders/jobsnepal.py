# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import MerojobItem


class JobsnepalSpider(scrapy.Spider):
    name = 'jobsnepal'
    start_urls = ['https://www.jobsnepal.com/']

    def parse(self, response):
        items = MerojobItem()
        jn_company = response.css('#main-content .job-item::text').extract()
        t_jn_company = []
        t_jn_job_title = []
        for i in jn_company:
           j = re.sub(r"\s+\s+", "", i)
           t_jn_company.append(j)
           print(t_jn_company)
        jn_job_title = response.css('.joblist::text').extract()
        for i in jn_job_title:
            j = re.sub(r"\s+\s+", "", i)
            t_jn_job_title.append(j)
            print(t_jn_job_title)
        jn_deadline = response.css('#main-content span::text').extract()
        items['jn_company'] = t_jn_company
        items['jn_job_title'] = t_jn_job_title
        items['jn_deadline'] = jn_deadline
        yield items
