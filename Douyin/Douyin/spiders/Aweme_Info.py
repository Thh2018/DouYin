# -*- coding: utf-8 -*-
import json

import scrapy

from ..items import *


# from Douyin.tools.Encrypt import get_aweme_token



class AwemeInfoSpider(scrapy.Spider):
    name = 'AwemeInfo'
    IDlist = [84064249580]
    scrawl_ID = set(IDlist)  # 记录待爬的用户ID
    finish_ID = set()  # 记录已爬的用户ID

    def __init__(self):
        """变化参数：max_time  user_id mas as ts"""

        self.base_url = 'http://aweme.snssdk.com/'
        self.api = 'v1/user/'
        self.params = 'iid=42814084050&ac=WIFI&os_api=18&app_name=aweme&channel=App%20Store&idfa=E4EB265C-1B1F-4570-B239-16D9429E7517&device_platform=iphone&build_number=25105&vid=59C7B0FB-E25F-40FE-81FE-A4D6BE9F5BE3&openudid=c8c332e2c9d8c524bc7eb7b302d72a287d614eb7&device_type=iPhone7,1&app_version=2.5.1&device_id=53384867487&version_code=2.5.1&os_version=10.3.3&screen_width=1125&aid=1128&user_id=84064249580&mas=0177d21c2eeff8271994d548a5097d66eabd5337114b83652fd6a8&as=a1450b5804778b882c4718&ts=1535948916'
        # url = self.base_url + self.api + "?" + self.params
        self.start_url = 'https://aweme.snssdk.com/aweme/v1/aweme/post/?iid=42814084050&ac=WIFI&os_api=18&app_name=aweme&channel=App%20Store&idfa=E4EB265C-1B1F-4570-B239-16D9429E7517&device_platform=iphone&build_number=25105&vid=59C7B0FB-E25F-40FE-81FE-A4D6BE9F5BE3&openudid=c8c332e2c9d8c524bc7eb7b302d72a287d614eb7&device_type=iPhone7,1&app_version=2.5.1&device_id=53384867487&version_code=2.5.1&os_version=10.3.3&screen_width=1125&aid=1128&count=21&max_cursor=0&min_cursor=0&user_id=84064249580&mas=01f00431784a7703778521ff986e79cf6100d31db8c0749697ccf1&as=a1152d48a8c44b6adc7540&ts=1535957576'

    def start_requests(self):
        # while self.scrawl_ID.__len__():
        # ID = self.scrawl_ID.pop()
        # self.finish_ID.add(ID)
        # ID = str(ID)
        # start_url = self.start_url.format(ID)

        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        item = AwemeInfoItem()
        data = json.loads(response.body.decode())
        aweme_lists = data["aweme_list"]
        max_cuosor = data['max_cuosor']
        has_more = data['has_more']
        for aweme_list in aweme_lists:
            item['author_user_id'] = aweme_list['author_user_id']  # 作者id
            aweme_info = aweme_list['statistics']  # 作品列表
            item['aweme_id'] = aweme_info['aweme_id']  # 作品id
            item['digg_count'] = aweme_info['digg_count']  # 作品点赞数
            item['comment_count'] = aweme_info['comment_count']  # 作品评论数
            item['share_count'] = aweme_info['share_count']  # 作品转发数
            yield item
        if has_more == 1:
            pass
