# -*- coding: utf-8 -*-

import json

import re
import scrapy

from ..querydata import QueryUserId
from ..items import *
from tools import Encrypt


class AwemeInfoSpider(scrapy.Spider):
    name = 'Follwers'

    def __init__(self, *args, **kwargs):
        super(AwemeInfoSpider, self).__init__(*args, **kwargs)
        """变化参数：max_time  user_id mas as ts"""

        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'http://aweme.snssdk.com'
        self.api = '/aweme/v1/user/following/list/'
        self.params = 'iid=42814084050&ac=WIFI&os_api=18&app_name=aweme&channel=App%20Store&idfa=E4EB265C-1B1F-4570-B239-16D9429E7517&device_platform=iphone&build_number=25105&vid=59C7B0FB-E25F-40FE-81FE-A4D6BE9F5BE3&openudid=c8c332e2c9d8c524bc7eb7b302d72a287d614eb7&device_type=iPhone7,1&app_version=2.5.1&device_id=53384867487&version_code=2.5.1&os_version=10.3.3&screen_width=1125&aid=1128&count=20&max_time=1536054232&user_id={}&mas=01a1c70831f92f6d1b7fb7812675477890c4f0f93a28b757d30ebe&as=a1859588e80d2b633e1303&ts=1536054232'
        self.url = self.base_url + self.api + "?" + self.params


    def start_requests(self):
        for user_id in self.User_ID_List:
            start_url = self.url.format(user_id[0])
            Encrypt.get_aweme_token(start_url)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    def parse(self, response):
        item = FansInfoItem()
        data = json.loads(response.body.decode())
        followings_lists = data["followings"]
        # 判断是否有下一页的参数
        has_more = data["has_more"]
        # 下一页url中的"max_time"为上一次json数据中的"min_time"
        max_time = str(data["min_time"])

        for followings_list in followings_lists:
            item["uid"] = followings_list["uid"]

        while has_more:
            url = re.sub("max_time=(\d+)", max_time, response.meta['url'])
            # 重新获取mas和as加密参数，返回一个url

            yield scrapy.Request(url, callback=self.parse)
