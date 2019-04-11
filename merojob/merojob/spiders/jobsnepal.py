# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import MerojobItem


class JobsnepalSpider(scrapy.Spider):
    name = 'jobsnepal'
    page_number =2
    start_urls = ['https://www.jobsnepal.com/premium-listings']


    def parse(self, response):
        items = MerojobItem()
        jn_company = response.css('#main-content .job-item::text').extract()
        t_jn_company = []
        t_jn_job_title = []
        for i in jn_company:
           j = re.sub(r"\s+\s+", "", i)
           t_jn_company.append(j)

        jn_job_title = response.css('.joblist::text').extract()
        for i in jn_job_title:
            j = re.sub(r"\s+\s+", "", i)
            t_jn_job_title.append(j)

        jn_deadline = response.css('#main-content span::text').extract()
        items['jn_company'] = t_jn_company
        items['jn_job_title'] = t_jn_job_title
        items['jn_deadline'] = jn_deadline
        yield items

        next_page ='https://www.jobsnepal.com/premium-listings/page-'+str(JobsnepalSpider.page_number)
        print(next_page)

        if JobsnepalSpider.page_number <= 100:
            print(JobsnepalSpider.page_number)
            JobsnepalSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)
