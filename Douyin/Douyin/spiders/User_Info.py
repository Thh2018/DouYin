# -*- coding: utf-8 -*-
# 运行环境：Python3.6

import json

import scrapy

from ..items import UserInfoItem
from ..querydata import QueryUserId
from tools import Encrypt


class FansSpider(scrapy.Spider):
    name = 'UserInfo'

    def __init__(self, *args, **kwargs):
        """变化参数：max_time  user_id mas as ts"""

        super(FansSpider, self).__init__(*args, **kwargs)
        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'https://api.amemv.com'
        self.api = '/aweme/v1/user/'
        self.params = "user_id={}&retry_type=no_retry&iid=42630256117&device_id=36329111283&ac=wifi&channel=oppo&aid=1128&app_name=aweme&version_code=251&version_name=2.5.1&device_platform=android&ssmix=a&device_type=OPPO+R7s&device_brand=OPPO&language=zh&os_api=19&os_version=4.4.4&uuid=867789024190969&openudid=26915c3d7a07b351&manifest_version_code=251&resolution=1080*1800&dpi=480&update_version_code=2512&_rticket=1536063656637&ts=1536063656&as=a14597c8d8ca6be89e4355&cp=7ca9b55089e08582e1_uMy&mas=0135bf53857ba449ab6128d468a2c9f0fdacaccc2ca69c1ca6466c"
        self.url = self.base_url + self.api + "?" + self.params

    def start_requests(self):
        for user_id in self.User_ID_List:
            start_url1 = self.url.format(user_id[0])
            start_url = Encrypt.get_aweme_token(start_url1)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    def parse(self, response):
        item = UserInfoItem()
        data = json.loads(response.body.decode())
        user_info = data["user"]

        item["nickname"] = user_info['nickname']  # 用户名
        item["uid"] = user_info['uid']  # 用户id
        item["short_id"] = user_info['short_id']  # 用户短id
        item["unique_id"] = user_info['unique_id']  # 自定义id
        item["unique_id_modify_time"] = user_info[
            'unique_id_modify_time']  # 自定义id修改时间
        item["total_favorited"] = user_info['total_favorited']  # 抖音总获赞数
        followers_detail = user_info["followers_detail"]
        item["aweme_fans_count"] = followers_detail[0]['fans_count']  # 抖音粉丝数
        item["aweme_apple_id"] = followers_detail[0]['apple_id']  # 抖音apple_id
        item["toutiao_fans_count"] = followers_detail[1]['fans_count']  # 头条粉丝数
        item["toutiao_apple_id"] = followers_detail[1]['apple_id']  # 头条apple_id
        item["live_stream_aweme_fans_count"] = followers_detail[2][
            'fans_count']  # 火山粉丝数
        item["live_stream_apple_id"] = followers_detail[2][
            'apple_id']  # 火山apple_id
        item["aweme_count"] = user_info['aweme_count']  # 抖音作品数
        item["favoriting_count"] = user_info['favoriting_count']  # 抖音喜欢作品数

        # 性别
        gender = user_info['gender']
        if gender == 1:
            item["gender"] = '男'
        elif gender == 0:
            item["gender"] = '女'
        avatar_larger = user_info["avatar_larger"]
        item["avatar_larger_url"] = avatar_larger["url_list"][0]  # 头像url
        item["avatar_larger_uri"] = avatar_larger["uri"]  # 头像uri
        item["weibo_name"] = user_info["weibo_name"]  # 绑定微博
        item["school_name"] = user_info['school_name']  # 学校名称
        item["school_poi_id"] = user_info['school_poi_id']  # 学校POI ID
        item["school_type"] = user_info['school_type']  # 学校类型
        item["location"] = user_info['location']  # 位置
        item["birth"] = user_info['birthday']  # 出生日期
        item["constellation"] = user_info['constellation']  # 星座
        item["city"] = user_info['city']  # 城市
        item["signature"] = user_info['signature']  # 个性签名
        login_platform = user_info['login_platform']  # 登录方式
        if login_platform == 0:
            item["login_platform"] = "手机号"
        elif login_platform == 4:
            item["login_platform"] = "QQ"
        elif login_platform == 5:
            item["login_platform"] = "微信"
        elif login_platform == 6:
            item["login_platform"] = "微博"
        else:
            item["login_platform"] = "其他"
        item["realname_verify_status"] = user_info[
            'realname_verify_status']  # 实名验证状态
        item["is_block"] = user_info['is_block']  # 是否被锁
        item["custom_verify"] = user_info['custom_verify']  # 个人认证
        item["verify_info"] = user_info['verify_info']  # 认证信息
        item["real_name_verify_status"] = user_info[
            'realname_verify_status']  # 是否是实名认证
        item["is_ad_fake"] = user_info['is_ad_fake']  # 是否是假广告？
        item["is_gov_media_vip"] = user_info['is_gov_media_vip']  # 是否是政府单位媒体
        item["is_verified"] = user_info['is_verified']  # 是否验证过
        item["live_agreement"] = user_info['live_agreement']  # 合同？
        item["live_verify"] = user_info['live_verify']  # 线下认证？
        # 企业认证原因
        item["enterprise_verify_reason"] = user_info['enterprise_verify_reason']
        item["commerce_user_level"] = user_info['commerce_user_level']  # 商务等级
        item["user_canceled"] = user_info['user_canceled']
        item["with_commerce_entry"] = user_info['with_commerce_entry']
        item["with_dou_entry"] = user_info['with_dou_entry']
        item["with_douplus_entry"] = user_info['with_douplus_entry']
        item["with_fusion_shop_entry"] = user_info['with_fusion_shop_entry']
        item["with_new_goods"] = user_info['with_new_goods']
        item["with_shop_entry"] = user_info['with_shop_entry']
        item["need_recommend"] = user_info['need_recommend']
        item["room_id"] = user_info['room_id']
        item["special_lock"] = user_info['special_lock']

        return item
