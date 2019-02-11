# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/11 15:39
import json
from public.publicExcel import PublicExcel
from public.publicYaml import PublicGetYaml
from public.publicDingDing import PublicDingDing
from insurance.insuranceOpera import InsuranceOpera
from insurance.insuranceTime import InsuranceTime
from insurance.insuranceLoginCookies import InsuranceLoginCookies
from runMain import RunMain

class RunOrders(object):
    def __init__(self,path,yaml_path):
        self.uri = PublicGetYaml(yaml_path).get_Yaml()['caseOrders']['uri']
        self.companyCode = PublicGetYaml(yaml_path).get_Yaml()['caseOrders']['companyCode']
        self.insCompany = PublicGetYaml(yaml_path).get_Yaml()['caseOrders']['insCompany']
        self.dingding = PublicGetYaml(yaml_path).get_Yaml()['dingding']['token']
        self.holder = PublicGetYaml(yaml_path).get_Yaml()['holder']
        self.excel = PublicExcel(path)
        self.opera = InsuranceOpera(path)
        self.time = InsuranceTime()
        self.cookie = InsuranceLoginCookies()
        self.main = RunMain()
        self.message = PublicDingDing()

    def InsuranceDate(self):
        #方法获取的参数(年:3,月:2,日:1)
        case_productBeginDate= ''
        case_productEndDate=''
        excel_count = self.excel.get_lines(0)
        for num in range(1,excel_count):
            case_run = self.opera.get_productRun(num)
            if case_run == 'yes':
                if int(self.opera.get_productValue(num)) == 1 and  int(self.opera.get_productType(num)) == 3 :
                    day = 1
                    case_productBeginDate = self.time.policyBeginDate(day)
                    case_productEndDate = self.time.policyEndDate(day+364)
                elif int(self.opera.get_productValue(num)) == 1 and  int(self.opera.get_productType(num)) == 1 :
                    case_productBeginDate = self.time.policyBeginDate(day)
                    case_productEndDate = self.time.policyEndDate(day+7)
        return  case_productBeginDate,case_productEndDate

    def InsuranceOrdersRun(self):
        excel_count = self.excel.get_lines(0)
        for num in range(1,excel_count):
            case_run = self.opera.get_productRun(num)
            if case_run == 'yes':
                print num
                #从case获取的参数
                case_productName = str(self.opera.get_productName(num))
                case_productCode = str(self.opera.get_productCode(num))
                case_productValue = int(self.opera.get_productValue(num))
                case_productType = str(self.opera.get_productType(num))
                case_productPrice = str(self.opera.get_productPrice(num))
                case_productPlanName = str(self.opera.get_productPlanName(num))
                case_productHealth = str(self.opera.get_productHealth(num))
                case_productUrl = str(self.opera.get_productUrl(num))
                case_productRequest = str(self.opera.get_productRequest(num))
                case_productExpect = str(self.opera.get_productExpect(num))
                case_productoPenid=str(self.cookie.get_login_result()[0])
                case_productToken=str(self.cookie.get_login_result()[1])
                self.cookies=self.cookie.get_login_result()[2]
                age = ""
                beneficiary=97
                policyBeginDate=self.InsuranceDate()[0]
                policyEndDate=self.InsuranceDate()[1]
                productNum=1
                relationshipWithHolder=1
                self.url1=case_productUrl+"age=%s&beneficiary=%s&companyCode=%s&health=%s&holderBirthday=%s&holderEmail=%s&holderMobile=%s&holderName=%s&holderPaperCat=%s&holderPaperNo=%s&holderSex=%s&insCompany=%s&insurePeriod=%s&insurePeriodType=%s&insuredBirthday=%s&insuredEmail=%s&insuredMobile=%s&insuredName=%s&insuredPaperCat=%s&insuredPaperNo=%s&insuredSex=%s&openid=%s&planName=%s&policyBeginDate=%s&policyEndDate=%s&productCode=%s&productName=%s&productNum=%s&productUnitPrice=%s&relationshipWithHolder=%s&token=%s&totalPrice=%s"%(age,beneficiary,self.companyCode,case_productHealth,self.holder['holderBirthday'],self.holder['holderEmail'],self.holder['holderMobile'],self.holder['holderName'],self.holder['holderPaperCat'],self.holder['holderPaperNo'],self.holder['holderSex'],self.insCompany,case_productValue,case_productType,self.holder['holderBirthday'],self.holder['holderEmail'],self.holder['holderMobile'],self.holder['holderName'],self.holder['holderPaperCat'],self.holder['holderPaperNo'],self.holder['holderSex'],case_productoPenid,case_productPlanName,policyBeginDate,policyEndDate,case_productCode,case_productName,productNum,case_productPrice,relationshipWithHolder,case_productToken,case_productPrice)
                res_result =self.main.run_main(case_productRequest,self.url1,cookies=self.cookies)
                res_time = self.main.run_time(case_productRequest,case_productUrl,cookies=self.cookies)
                self.excel.write_excel(0,num,12,res_result)
                self.excel.write_excel(0,num,13,res_time)
                if case_productExpect in res_result:
                    self.excel.write_excel(0,num,14,'pass')
                else:
                    self.excel.write_excel(0,num,14,'fail')
                    #失败把请求和响应发送到钉钉
                    result = u"请求数据:"+str(self.url1)+u"------------>"+u"请求响应:"+str(res_time)
                    self.message.get_message(self.dingding,result)
            else:
                print u"打印:%s"%num



if __name__ == '__main__':
    path = '../config/case.xls'
    yaml_path = "../config/orderParameter.yaml"
    orders = RunOrders(path,yaml_path)
    orders.InsuranceOrdersRun()
