import random
import requests
import time

#url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
content='我们'


class Youdao():
    def __init__(self, content):
        self.content = content
        self.url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        self.ts = self.get_ts()
        self.salt = self.get_salt()
        self.sign = self.get_sign()

    def get_salt(self):
        s = str(random.randint(0, 10))
        t = self.ts
        return t + s

    def get_md5(self, value):
        import hashlib
        m = hashlib.md5()
        m.update(value.encode("utf-8"))
        return m.hexdigest()

    def get_sign(self):
        i = self.salt
        e = self.content
        s = "fanyideskweb" + e + i + "Nw(nmmbP%A-r6U3EUn]Aj"
        # print("s=",s,"   md5=",get_md5(s))
        return self.get_md5(s)

    # return 'd330b7eeeef6a968524d0ea22f41a6f2'

    def get_ts(self):
        t = time.time()
        ts = str(int(round(t * 1000)))
        print("ts=", ts)
        return ts

    # def get_content(self):
    # return content

    def yield_form_date(self):
        form_data = {
            'i': self.content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '8c5f607603b502c5c8a878c67f338978',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
        }
        return form_data

    def get_headers(self):
        headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=536859492@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=792170873.3165163; JSESSIONID=aaatqjQNPemuYhdZsuYfx; ___rl__test__cookies=1586760868588',
            'Referer': 'http: // fanyi.youdao.com /',
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/78.0.3904.63Safari/537.36',
        }
        return headers

    def fanyi(self):
        response = requests.post(self.url, data=self.yield_form_date(), headers=self.get_headers())
        return response.text


if __name__ == '__main__':
    youdao=Youdao('我们')
    print(youdao.fanyi())
