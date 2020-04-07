import random
import requests
import time
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    return  t+s


def get_sign():
    return 'd330b7eeeef6a968524d0ea22f41a6f2'


def get_ts():
    t=time.time()
    ts=str(int(round(t*1000)))
    return ts


form_data={
    'i': '我和你',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': '8c5f607603b502c5c8a878c67f338978',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
}
response=requests.post(url,form_data)
print(response.text)