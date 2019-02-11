# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/3 16:22
# *_*coding:utf-8 *_*
import logging,os,time

cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'logs')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path): os.mkdir(log_path)
class PublicLogs:

    def __init__(self):
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #输入日志格式
        self.formatter=logging.Formatter('%(asctime)s -%(filename)s - %(levelname)s: %(message)s ')

    def __console(self,level,message):
        #创建FileHandle存于本地
        logfile='../logs/log.txt'
        fh=logging.FileHandler(logfile,'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建streamhandler输入在控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)



        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

        #防止重复打印
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)

        fh.close()

    def info(self,message):
        self.__console('info',message)

    def debug(self,message):
        self.__console('debug',message)

    def warning(self,message):
        self.__console('warning',message)

    def error(self,message):
        self.__console('error',message)

if __name__ == '__main__':
    log=PublicLogs()
    log.info(u"------测试开始----------")
    log.error(u"-----测试异常----------")




