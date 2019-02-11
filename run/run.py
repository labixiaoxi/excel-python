# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/14 13:56
from insurance.insuranceParameter import  InsuranceParameter
from runOrders import RunOrders
from public.publicLogs import PublicLogs
log = PublicLogs()
class Run(object):
    def run(self):
        """
        获取参数,发起请求
        :return:
        """
        path = "../config/case.xls"
        yaml_path = '../config/orderParameter.yaml'
        log.info(u"-------------start----------------------------")
        InsuranceParameter(path,yaml_path).productCode()
        InsuranceParameter(path,yaml_path).productDetails()
        InsuranceParameter(path,yaml_path).productPrice()
        RunOrders(path,yaml_path).InsuranceOrdersRun()
        log.info(u"-------------end----------------------------")


if __name__ == '__main__':
    run = Run()
    run.run()