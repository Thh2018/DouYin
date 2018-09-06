# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 用户个人信息
class UserInfoItem(scrapy.Item):
    nickname = scrapy.Field()  # 用户名
    uid = scrapy.Field()  # 用户ID
    short_id = scrapy.Field()  # 用户短ID
    unique_id = scrapy.Field()  # 自定义ID
    unique_id_modify_time = scrapy.Field()  # 自定义ID修改时间
    total_favorited = scrapy.Field()  # 抖音总获赞数
    aweme_fans_count = scrapy.Field()  # 抖音粉丝数
    aweme_apple_id = scrapy.Field()  # 抖音apple_id
    toutiao_fans_count = scrapy.Field()  # 头条粉丝数
    toutiao_apple_id = scrapy.Field()  # 头条apple_id
    live_stream_aweme_fans_count = scrapy.Field()  # 火山小视频粉丝数
    live_stream_apple_id = scrapy.Field()  # 火山apple_id
    aweme_count = scrapy.Field()  # 抖音作品数量
    favoriting_count = scrapy.Field()  # 抖音喜欢作品数

    gender = scrapy.Field()  # 性别
    avatar_larger_url = scrapy.Field()  # 头像url
    avatar_larger_uri = scrapy.Field()  # 头像uri
    weibo_name = scrapy.Field()  # 绑定微博
    school_name = scrapy.Field()  # 学校名称
    school_poi_id = scrapy.Field()  # 学校POI ID
    school_type = scrapy.Field()  # 学校类型
    location = scrapy.Field()  # 位置
    birth = scrapy.Field()  # 出生日期
    constellation = scrapy.Field()  # 星座
    city = scrapy.Field()  # 城市
    signature = scrapy.Field()  # 个性签名
    login_platform = scrapy.Field()  # 登录方式

    realname_verify_status = scrapy.Field()  # 实名验证状态
    is_block = scrapy.Field()  # 是否被锁
    custom_verify = scrapy.Field()  # 个人认证
    verify_info = scrapy.Field()  # 认证信息
    real_name_verify_status = scrapy.Field()  # 是否是实名认证
    is_ad_fake = scrapy.Field()  # 是否是假广告？
    is_gov_media_vip = scrapy.Field()  # 是否是政府单位媒体
    is_verified = scrapy.Field()  # 是否验证过
    live_agreement = scrapy.Field()  # 合同？
    live_verify = scrapy.Field()  # 线下认证？
    enterprise_verify_reason = scrapy.Field()  # 企业认证原因
    commerce_user_level = scrapy.Field()  # 商务等级

    user_canceled = scrapy.Field()  #
    with_commerce_entry = scrapy.Field()  #
    with_dou_entry = scrapy.Field()  #
    with_douplus_entry = scrapy.Field()  #
    with_fusion_shop_entry = scrapy.Field()  #
    with_new_goods = scrapy.Field()  #
    with_shop_entry = scrapy.Field()  #
    need_recommend = scrapy.Field()  #
    room_id = scrapy.Field()  #
    special_lock = scrapy.Field()  #


# 作品列表信息
class AwemeInfoItem(scrapy.Item):
    author_user_id = scrapy.Field()  # 作者ID
    aweme_id = scrapy.Field()  # 作品ID
    aweme_type = scrapy.Field()  # 作品类型
    create_time = scrapy.Field()  # 创建时间
    duration = scrapy.Field()  # 持续时间
    desc = scrapy.Field()  # 作品描述
    digg_count = scrapy.Field()  # 点赞数
    comment_count = scrapy.Field()  # 评论数
    share_count = scrapy.Field()  # 转发数

    is_ads = scrapy.Field()  # 是否是广告
    is_fantasy = scrapy.Field()
    is_hash_tag = scrapy.Field()
    is_pgcshow = scrapy.Field()  # 是否为pgc显示
    is_relieve = scrapy.Field()
    is_top = scrapy.Field()  # 是否置顶
    is_vr = scrapy.Field()  # 是否是VR视频
    is_del_video = scrapy.Field()  # 是否删除视频
    redirect = scrapy.Field()  # 是否重定向
    item_comment_settings = scrapy.Field()  # 评论设置
    prevent_download = scrapy.Field()  # 是否禁止下载
    rate = scrapy.Field()  # 比率
    region = scrapy.Field()  # 区域
    share_url = scrapy.Field()  # 分享链接
    sort_label = scrapy.Field()  # 分类标签


    # 背景音乐信息
    music_album = scrapy.Field()  # 音乐专辑
    music_author = scrapy.Field()  # 音乐作者
    author_deleted = scrapy.Field()  # 作者是否删除
    collect_stat = scrapy.Field()  # 值为0
    cover_hd = scrapy.Field()  # 封面高清图片地址
    cover_large = scrapy.Field()  # 封面大图地址
    cover_medium = scrapy.Field()  # 封面中图地址
    cover_thumb = scrapy.Field()  # 封面小图地址
    is_original = scrapy.Field()  # 是否为原创
    id = scrapy.Field()  # 音乐ID
    is_restricted = scrapy.Field()  # 是否保密
    is_video_self_see = scrapy.Field()  # 是否只有自己可看
    mid = scrapy.Field()  # mid
    owner_handle = scrapy.Field()  # 作者自定义ID
    owner_id = scrapy.Field()  # 作者ID
    offline_desc = scrapy.Field()  # 线下描述
    play_url = scrapy.Field()  # 音乐播放地址
    source_platform = scrapy.Field()  # 来源平台？
    status = scrapy.Field()  # 状态
    title = scrapy.Field()  # 背景音乐名称
    user_count = scrapy.Field()  # 使用数量

    # 视频信息
    bit_rate = scrapy.Field()  # 比特率

    # 风险信息
    content = scrapy.Field()
    risk_sink = scrapy.Field()
    type = scrapy.Field()
    warn = scrapy.Field()


# 粉丝信息
class FansInfoItem(scrapy.Item):
    uid = scrapy.Field()  # 用户ID


class CommentInfoItem(scrapy.Item):
    aweme_id = scrapy.Field()  # 作品ID
    create_time = scrapy.Field()  # 评论时间
    text = scrapy.Field()  # 评论内容
    user_id = scrapy.Field()  # 评论ID
    total = scrapy.Field()  # 评论总数
