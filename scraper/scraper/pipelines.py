# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import os
import psycopg2


class ScraperPipeline:
    def __init__(self):
        ## Connection Details
        hostname = os.environ.get('POSTGRES_HOST')
        username = os.environ.get('POSTGRES_USER')
        password = os.environ.get('POSTGRES_PASSWORD')
        database = os.environ.get('POSTGRES_NAME')
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        self.cursor.execute(""" insert into web_listing (title, image_url) values (%s,%s)""", (
            item["title"],
            item["image_url"],
        ))
        self.connection.commit()
        return item
