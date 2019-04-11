# -*- coding: utf-8 -*-
import mysql.connector


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MerojobPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='job'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS job_list""")
        self.curr.execute("""create table job_list(jn_company text, jn_job_title text)""")


    def process_item(self, item, spider):
        # print("\n\n\n\n\n\n\pugypppp\n\n\n\n\n")
        self.store_db(item)
        return item

    def store_db(self, item):
        # print("----------------------------------------------------\n",item,'-------------------------------------------')
        for index, elem in enumerate(item['company_name']):
            self.curr.execute("""insert into job_list values (%s,%s)""", (
                item['company_name'][index],
                item['company_vacancy'][index],
            ))

        self.conn.commit()

    # def process_item(self, item, spider):
    #     # print(item)
    #     # print("pipeline: ", + item['company_name'][0])
    #     return item