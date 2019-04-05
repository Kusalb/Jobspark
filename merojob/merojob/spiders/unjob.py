# -*- coding: utf-8 -*-
import re
import scrapy
from ..items import MerojobItem


class UnJobSpider(scrapy.Spider):
    name = 'unjob'
    page_number = 1
    start_urls = ['https://unjobs.org']

    def parse(self, response):
        items = MerojobItem()
        uj_company = response.css('.jtitle::text').extract()
        t_uj_company = []
        t_uj_job_title = []
        t_uj_deadline = []


        for i in uj_company:
            j = re.sub(r"\s+\s+", "", i)
            t_uj_company.append(j)

        uj_job_title = response.css('.jtitle::text').extract()
        for i in uj_job_title:
            j = re.sub(r"\s+\s+", "", i)
            t_uj_job_title.append(j)

        uj_deadline = response.css('.job span').css('::text').extract()
        for i in uj_deadline:
            j = re.sub(r"\s+\s+","",i)
            t_uj_deadline.append(j)


        t2_uj_deadline = [x for x in t_uj_deadline if x]

        items['uj_company'] = t_uj_company
        items['uj_job_title'] = t_uj_job_title
        items['uj_deadline'] = t2_uj_deadline
        yield items

        # next_page = 'https://unjobs.org/new/'+ str(UnJobSpider.page_number)
        # if UnJobSpider.page_number <=40:
        #     yield response.follow(next_page, callback = self.parse)
            

