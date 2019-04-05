# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MerojobItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    company_vacancy = scrapy.Field()
    imagelink = scrapy.Field()

    jn_company = scrapy.Field()
    jn_job_title = scrapy.Field()
    jn_deadline = scrapy.Field()

    kj_company = scrapy.Field()
    kj_job_title = scrapy.Field()
    kj_deadline = scrapy.Field()

    uj_company =scrapy.Field()
    uj_job_title = scrapy.Field()
    uj_deadline = scrapy.Field()
    pass
