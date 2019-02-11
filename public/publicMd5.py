# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2018/4/2 16:18
from public.publicLogs import PublicLogs
import hashlib
log = PublicLogs()
class PublicMd5:
    def md5(self,key):
        result=hashlib.md5()
        result.update(key)
        result_code=result.hexdigest()
        log.info(u"需要加密的参数:%s,解密后的值:%s"%(key,result_code))
        return result_code

if __name__== '__main__':
    m=PublicMd5()
    m.md5('jhj123456')