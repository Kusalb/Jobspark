# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import MerojobItem

class MerojobSpiderSpider(scrapy.Spider):
    name = 'merojob'
    start_urls = ['https://merojob.com/']

    def parse(self, response):
        items = MerojobItem()
        company_name = response.css('.font-md-xxs::text').extract()
        comp_name = []
        comp_vacancy =[]
        f_comp_name =[]
        f_comp_vacancy = []
        for i in company_name:
            j = re.sub(r"\s+\s+", "", i)
            comp_name.append(j)

        company_vacancy = response.css('.hover-primary span::text').extract()
        for i in company_vacancy:
            j = re.sub(r"\s+\s+", "", i)
            comp_vacancy.append(j)

        f_comp_name = [x for x in comp_name if x]
        f_comp_vacancy = [x for x in comp_vacancy if x]

        imagelink = response.css('.shadow::attr(src)').extract()
        job = response.css('.no-gutters .media-body::text').extract()

        items['company_name'] = f_comp_name
        items['company_vacancy'] = f_comp_vacancy
        items['imagelink'] = imagelink
        # items['job'] = job
        # print(company_name)
        yield items