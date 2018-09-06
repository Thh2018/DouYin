# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .items import *


class DouyinPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        if isinstance(item, UserInfoItem):
            self.client.Douyin.UserInfo.insert_one(dict(item))
            return item
        elif isinstance(item, AwemeInfoItem):
            self.client.Douyin.AwemeInfo.insert_one(dict(item))
            return item
        elif isinstance(item, FansInfoItem):
            self.client.Douyin.FansInfo.insert_one(dict(item))
        elif isinstance(item, CommentInfoItem):
            self.client.Douyin.CommentInfo.insert_one(dict(item))

    def close_spider(self, spider):
        self.client.close()
