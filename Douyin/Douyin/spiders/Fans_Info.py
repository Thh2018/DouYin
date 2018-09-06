# -*- coding: utf-8 -*-
import json

import re
import scrapy

from ..querydata import QueryUserId
from ..items import *
from tools import Encrypt


class AwemeInfoSpider(scrapy.Spider):
    name = 'Fans'

    def __init__(self, *args, **kwargs):
        super(AwemeInfoSpider, self).__init__(*args, **kwargs)
        """变化参数：max_time  user_id mas as ts"""

        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'https://api.amemv.com'
        self.api = '/aweme/v1/user/follower/list/'
        self.params = "user_id=84064249580&max_time=1536062140&count=20&retry_type=no_retry&iid=42630256117&device_id=36329111283&ac=wifi&channel=oppo&aid=1128&app_name=aweme&version_code=251&version_name=2.5.1&device_platform=android&ssmix=a&device_type=OPPO+R7s&device_brand=OPPO&language=zh&os_api=19&os_version=4.4.4&uuid=867789024190969&openudid=26915c3d7a07b351&manifest_version_code=251&resolution=1080*1800&dpi=480&update_version_code=2512&_rticket=1536062140613&ts=1536062142&as=a1950778ceab8bb20e4355&cp=74b2bb5ae2e38929e1OuWy&mas=015d5bedcaf2ab161a91bb9dd107ca6c99acaccc2ca60c4c46461c"
        self.url = self.base_url + self.api + "?" + self.params

    def start_requests(self):
        # for user_id in self.User_ID_List:
        #     start_url = self.url.format(user_id[0])
        start_url = Encrypt.get_aweme_token(self.url)
        yield scrapy.Request(url=start_url, callback=self.parse,
                             meta={'url': start_url})

    def parse(self, response):
        item = FansInfoItem()
        data = json.loads(response.body.decode())
        fans_lists = data["followers"]
        # 判断是否有下一页的参数
        has_more = data["has_more"]
        # 下一页url中的"max_time"为上一次json数据中的"min_time"
        max_time = str(data["min_time"])

        for fan_list in fans_lists:
            item["uid"] = fan_list["uid"]

        while has_more:
            url = re.sub("max_time=(\d+)", max_time, response.meta['url'])
            # 重新获取mas和as加密参数，返回一个url

            yield scrapy.Request(url, callback=self.parse)
