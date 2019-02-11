# *_*coding:utf-8 *_* 
import  requests,os,re
from public.publicLogs import PublicLogs
from public.publicYaml import PublicGetYaml
log = PublicLogs()
class InsuranceLoginCookies:
    def __init__(self):
        self.uri="http://59.110.171.83:9095/jhj-hyb-consumer-web/"
    # 重定向
    def get_real_url(self,url,try_count = 1):
        http_headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0"}
        if try_count > 3:
            return url
        try:
            rs = requests.get(url,headers=http_headers,timeout=10)
            if rs.status_code > 400:
                return self.get_real_url(url,try_count+1)
            return rs.url
        except:
            return self.get_real_url(url, try_count + 1)

    def get_login_result(self):
        self.url="/dpt/app?sign=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb3VyY2UiOiJhcHAiLCJ1c2VySWQiOjU0Mzk0MjA5NjQ5MTUxNTkwNCwibW9iaWxlIjoiMTc3NDg3NzYzNDYiLCJtYWMiOiI5MGQwMmFjZDJhMGY0MWQ4In0.3d6oHoTLGkWjT3o-l76DnNo7znNpsxrZAOZCgjysk7k&type=jhj"
        urlLogin=self.get_real_url(self.uri+self.url)
        r=requests.get(url=self.uri+self.url,allow_redirects=False)
        insurance_login=re.compile('http:.*?openid=(.*?)&token=(.*?)&')
        insurance_login_result=re.findall(insurance_login,urlLogin)
        openid = insurance_login_result[0][0]
        token  = insurance_login_result[0][1]
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        log.info(u"openid:%s,token:%s,"%(openid,token))
        log.info(u"cookies:"+str(cookies))
        return openid,token,cookies

if __name__ == '__main__':
    insuranceLogin=InsuranceLoginCookies()
    print insuranceLogin.get_login_result()