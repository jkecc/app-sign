import os

import requests


def mt_sign():
    # url = "https://bbs.binmt.cc/plugin.php?id=k_misign:sign&operation=list&op=today"
    url = "https://bbs.binmt.cc/plugin.php?id=k_misign:sign&operation=qiandao&format=text&formhash=10ff8b9a"
    headers = {
        "Accept": "text/html, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 12; zh-cn; 23113RKC6C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/16.8.8 swan-mibrowser"
    }
    cookies = {
           "cQWy_2132_saltkey": "s1ousujT",
           "cQWy_2132_auth": os.environ["MT_APP_AUTH"],
    }

    res = requests.get(url=url, headers=headers, cookies=cookies)
    print(res.text)
