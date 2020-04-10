import random
import requests
import time

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content='我和你'

def get_salt():
    s=str(random.randint(0,10))
    t=get_ts()
    return  t+s

def get_md5(value):
    import hashlib
    m=hashlib.md5()
    m.update(value.encode("utf-8"))
    return m.hexdigest()

def get_sign():
    i=get_salt()
    e=get_content()
    s="fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
    print("s=",s,"   md5=",get_md5(s))
    return get_md5(s)
    # return 'd330b7eeeef6a968524d0ea22f41a6f2'


def get_ts():
    t=time.time()
    ts=str(int(round(t*1000)))
    return ts

def get_content():
    return content

form_data={
    'i': get_content(),
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

def get_headers():
    headers={
        'Cookie':'OUTFOX_SEARCH_USER_ID = 536859492 @ 10.108.160.19',
        'Referer':'http: // fanyi.youdao.com /',
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/78.0.3904.63Safari/537.36',
    }
    return headers



if __name__ == '__main__':
    ts=get_ts()
    print(form_data)
    print(get_headers())
    response = requests.post(url, date=form_data,header=get_headers())
    print(response.text)