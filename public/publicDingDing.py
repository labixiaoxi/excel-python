# *_*coding:utf-8 *_* 
import requests,json
class PublicDingDing(object):
    def __init__(self):
        pass

    def get_message(self,token,content):
            self.url = 'https://oapi.dingtalk.com/robot/send?access_token=%s'%token
            self.pagrem = {
                "msgtype": "text",
                "text": {
                    "content": content
                },
                "isAtAll": True
            }
            self.headers = {
                'Content-Type': 'application/json'
            }
            f = requests.post(url=self.url, data=json.dumps(self.pagrem), headers=self.headers)
