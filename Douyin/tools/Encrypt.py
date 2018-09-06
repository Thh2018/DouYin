# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 11:52
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Encrypt.py
# @Software: PyCharm
import time
import json
import requests
import hashlib
from urllib.parse import urlparse, parse_qs, urlencode


def get_aweme_token(url):
    timestamp = time.time()
    token_url = "http://47.97.186.56:4570/getascpmas41d8224167374f85994185cd7d68be88"
    parse_param = parse_qs(urlparse(url).query, keep_blank_values=True)
    data = {key: value[-1] for key, value in parse_param.items()}
    data.pop("mas")
    data.pop("cp")
    data.pop("as")
    data["_rticket"] = str(round(timestamp * 1000))
    data["ts"] = str(int(timestamp))
    ts_short = (str(int(timestamp)) + "504c53f18b834e8b9b853cc64628cd12").encode()
    param = {"dic": data, "device_id": data["device_id"], "ts_short": int(timestamp),
             "mykey": hashlib.md5(ts_short).hexdigest()}
    token = requests.post(token_url, data=json.dumps(param)).json()
    data["as"] = token["As"]
    data["mas"] = token["Mas"]
    data["cp"] = token["Cp"]
    return url.split("?")[0] + "?" + urlencode(data)


if __name__ in "__main__":
    url = "https://api.amemv.com/aweme/v1/aweme/favorite/?user_id=88832667622&max_cursor=0&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=MuMu&device_brand=Android&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024*576&dpi=192&update_version_code=1832&_rticket=1536213417686&ts=1536213420&as=a1b5ec697cea1ba1e04355&cp=c2a5b657cf099f1be1Uc]g&mas=008435bbf9b3a897df221b6a7f86e9c1e8acaccc2c0ca68c86468c"
    print(get_aweme_token(url))
