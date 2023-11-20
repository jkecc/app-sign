import requests
import os


def magicalapp_sign():
    url = "http://www.magicalapp.cn/user/api/signDays"
    headers = {
        "Token": os.environ["MAGICALAPP_TOKEN"],
        "Host": "www.magicalapp.cn",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/4.9.3"
    }

    res = requests.get(url=url, headers=headers)
    print(res.status_code, res.text)
