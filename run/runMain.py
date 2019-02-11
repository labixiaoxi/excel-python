# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2018/5/31 15:40
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""
verify=False是https的使用需要添加的
requests库是接口测试的库,
        post是参数+url
        get是url
写了一个post_mian的方法和get_main的方法
run_main方法通过参数来区分是post还是get方法
"""
class RunMain:
    def post_main(self,url,data=None,cookies=None):
        if cookies==None:
            res=requests.post(url,data=data,verify=False)
        else:
            res=requests.post(url=url,data=data,cookies=cookies,verify=False)
        return res
    def get_main(self,url,cookies=None):
        if cookies==None:
            res=requests.get(url,verify=False)
        else:
            res=requests.get(url=url,cookies=cookies,verify=False)
        return res

    def run_main(self,method,url,data=None,cookies=None):
        if method=='post':
            res=self.post_main(url,data,cookies)
        elif method=='get':
            res=self.get_main(url,cookies)
        text= res.text
        return text

    def run_time(self,method,url,data=None,cookies=None):
        if method=='post':
            res=self.post_main(url,data,cookies)
        elif method=='get':
            res=self.get_main(url,cookies)
        runtime= res.elapsed.total_seconds()
        return runtime

if __name__ == '__main__':
    run = RunMain()
    url = 'https://ecodeapi.yinuoinfo.com/ApiCMembers/login'
    data = {
        "email": "13683451092",
        "password": "123456",
        "device_sid": "55ef27fbf4adde00",
        "from": "android",
        "os": "Product%3A+rk3288%2C+CPU_ABI%3A+armeabi-v7a%2C+TAGS%3A+test-keys%2C+VERSION_CODES.BASE%3A+1%2C+MODEL%3A+HDX065%2C+SDK%3A+19%2C+VERSION.RELEASE%3A+4.4.4%2C+DEVICE%3A+rk3288%2C+DISPLAY%3A+rk3288-eng+4.4.4+KTU84Q+eng.hdxyh.20170220.113739+test-keys%2C+BRAND%3A+rockchip%2C+BOARD%3A+rk30sdk%2C+FINGERPRINT%3A+rockchip%2Frk3288%2Frk3288%3A4.4.4%2FKTU84Q%2Feng.hdxyh.20170211.113739%3Aeng%2Ftest-keys%2C+ID%3A+KTU84Q%2C+MANUFACTURER%3A+goodchip%2C+USER%3A+hdxyh&",
        "intranet_ip": "192.168.0.160",
        "domain": "ecodeapi.yinuoinfo.com",
        "version": "Aw_1.42",
        "beta_version": "1.42"
    }
    print run.run_main('post',url,data)
    print run.run_time('post',url,data)


