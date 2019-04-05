# -*- coding: utf-8 -*-
import re

import scrapy
from ..items import MerojobItem


class KumarijobSpider(scrapy.Spider):
    name = 'kumarijob'
    start_urls = ['https://www.kumarijob.com/']

    def parse(self, response):
        items = MerojobItem()
        kj_company = response.css('.col-md-3 .m-text-center a , #menus_desktopss .m-text-center a , .strong_compname_anc , .company a , h6.m-text-center a').css('::text').extract()
        t_kj_company = []
        t_kj_job_title = []
        t_kj_deadline = []


        for i in kj_company:
            j = re.sub(r"\s+\s+", "", i)
            t_kj_company.append(j)

        kj_job_title = response.css('.card-title a , #recent_jobs h6 a , #job-desc-font , a.m-text-center').css('::text').extract()
        for i in kj_job_title:
            j = re.sub(r"\s+\s+", "", i)
            t_kj_job_title.append(j)

        kj_deadline = response.css('.recent_jobs_time li , time').css('::text').extract()
        for i in kj_deadline:
            j = re.sub(r"\s+\s+","",i)
            t_kj_deadline.append(j)


        t2_kj_deadline = [x for x in t_kj_deadline if x]

        items['kj_company'] = t_kj_company
        items['kj_job_title'] = t_kj_job_title
        items['kj_deadline'] = t2_kj_deadline
        yield items
