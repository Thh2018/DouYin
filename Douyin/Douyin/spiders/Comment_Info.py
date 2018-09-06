# coding = utf-8
import json

import re
import scrapy
from ..items import *
from ..querydata import QueryUserId


class CommentInfoSpider(scrapy.Spider):
    name = 'CommentInfo'

    def __init__(self, *args, **kwargs):
        """变化参数：max_time  user_id mas as ts"""

        super(CommentInfoSpider, self).__init__(*args, **kwargs)
        # # 从数据库中获取作品ID
        # self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'http://aweme.snssdk.com'
        self.api = '/aweme/v1/comment/list/'
        self.params = (
            "http://aweme.snssdk.com/aweme/v1/comment/list/?iid=42814084050&ac=WIFI&os_api=18&app_name=aweme&channel=App%20Store&idfa=E4EB265C-1B1F-4570-B239-16D9429E7517&device_platform=iphone&build_number=25105&vid=59C7B0FB-E25F-40FE-81FE-A4D6BE9F5BE3&openudid=c8c332e2c9d8c524bc7eb7b302d72a287d614eb7&device_type=iPhone7,1&app_version=2.5.1&device_id=53384867487&version_code=2.5.1&os_version=10.3.3&screen_width=1125&aid=1128&aweme_id=6596152450577599751&comment_style=2&count=20&cursor=0&digged_cid=&mas=01253d6fd643be7b05e11839019fbd40b3b47659ca3811feac64ee&as=a1b57488e8128b054e8255&ts=1536050472")
        self.url = self.base_url + self.api + "?" + self.params

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        item = CommentInfoItem()
        data = json.loads(response.body.decode())
        has_more = data["has_more"]
        cursor = str(data["cursor"])
        comment_lists = data["comments"]
        for comment_list in comment_lists:
            item["aweme_id"] = comment_list["aweme_id"]  # 作品ID
            item["create_time"] = comment_list["create_time"]  # 评论时间
            item["text"] = comment_list["text"]  # 评论内容
            item["user_id"] = comment_list["user"]["uid"]  # 评论者ID
            item["total"] = data["total"]
            yield item
        while has_more:
            new_url = re.sub("cursor=(\d+)", cursor, self.url)  # 得到下一页评论信息
            yield scrapy.Request(url=new_url, callback=self.parse)
