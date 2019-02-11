# *_*coding:utf-8 *_* 
import requests
from insuranceLoginCookies import  InsuranceLoginCookies
from public.publicLogs import PublicLogs
from public.publicExcel import  PublicExcel
from public.publicYaml import PublicGetYaml
log =PublicLogs()

class InsuranceParameter:
    def __init__(self,path,yaml_path):
        self.id = InsuranceLoginCookies()
        self.excel = PublicExcel(path)
        self.uri=PublicGetYaml(yaml_path).get_Yaml()['caseOrders']['uri']


    def productCode(self):
        """
        获取产品的code
        :return:
        """
        categoryCode=1002  #从数据库获取
        loginMemberType=1
        productCode_list = []
        for page in range(1,3):
            self.url="product/products?categoryCode=%s&loginMemberType=%s&page=%s"%(categoryCode,loginMemberType,page)
            res = requests.get(url=self.uri+self.url)
            log.info(u"产品请求:%s"%self.url)
            log.info(u"产品响应:%s"%res.text)
            try:
                if res.status_code == 200:
                    data =len( res.json()['body']['datas'])
                    for i in range(data):
                        productListCommDesc = res.json()['body']['datas'][i]['productListCommDesc']
                        productCode = res.json()['body']['datas'][i]['productCode']
                        productCode_list.append(productCode)

            except:
                log.error(u"请求异常")
        return productCode_list

    def productDetails(self):
        """
        写入产品名称,产品编号,保障期间
        :return:
        """
        openid = str(self.id.get_login_result()[0])
        productCode = self.productCode()
        result_num=[]
        specificProductName_list = []
        specificProductCode_list = []
        specificProductValue_list = []
        specificProductType_list = []
        for code in productCode:
            self.url = "product/product?openid=%s&productCode=%s&"%(openid,code)
            res = requests.get(self.uri+self.url)
            log.info(u"%s产品的请求:%s"%(code,self.url))
            log.info(u"%s产品的响应:%s"%(code,res.text))
            plan_list = len(res.json()['body']['planList'])
            attrInfoList = len(res.json()['body']['attrInfoList'])
            #跳过不结佣产品
            if plan_list==0:
                continue
            result_num.append(plan_list)
            for i in range(plan_list):
                specificProductCode = res.json()['body']['planList'][i]['productCode']
                specificProductName = res.json()['body']['planList'][i]['productName']
                specificProductValue = res.json()['body']['attrInfoList'][attrInfoList-1]['attrValueList'][0]['value']
                specificProductType = res.json()['body']['attrInfoList'][attrInfoList-1]['attrValueList'][0]['valueType']
                log.info(u"产品名称:%s,产品编号:%s,产品保障期间:%s,产品保障类型:%s"%(specificProductName,specificProductCode,specificProductValue,specificProductType))
                specificProductCode_list.append(specificProductCode)
                specificProductName_list.append(specificProductName)
                specificProductValue_list.append(specificProductValue)
                specificProductType_list.append(specificProductType)
        #名称写入
        for name in range(len(specificProductName_list)):
            self.excel.write_excel(0,name+1,1,specificProductName_list[name])
        #编号写入
        for code in range(len(specificProductCode_list)):
            self.excel.write_excel(0,code+1,2,specificProductCode_list[code])
        #保障期间写入
        for value in range(len(specificProductValue_list)):
            self.excel.write_excel(0,value+1,3,specificProductValue_list[value])
        #保障类型写入
        for type in range(len(specificProductType_list)):
            self.excel.write_excel(0,type+1,4,specificProductType_list[type])




    def productPrice(self):
        specificProductPrice_list = []
        specificProductPlanName_list = []
        openid = str(self.id.get_login_result()[0])
        lenId = self.excel.get_ncols(0)
        for code in range(lenId):
            productCode =  self.excel.get_value(0,code+1,2)
            self.url= "product/product?openid=%s&productCode=%s"%(openid,productCode)
            res = requests.get(self.uri+self.url)
            log.info(u"产品编号:%s请求:%s"%(productCode,self.url))
            log.info(u"产品编号:%s响应:%s"%(productCode,res.text))
            price = res.json()['body']['defaultShowPrice']
            specificProductPrice_list.append(price)

            planName = res.json()['body']['planName']
            specificProductPlanName_list.append(planName)
        #金额写入
        for price in range(len(specificProductPrice_list)):
            self.excel.write_excel(0,price+1,5,specificProductPrice_list[price])
        #产品保额写入
        for planName in range(len(specificProductPlanName_list)):
            self.excel.write_excel(0,planName+1,6,specificProductPlanName_list[planName])




if __name__ == '__main__':
    orders=InsuranceParameter('../config/case.xls','../config/orderParameter.yaml')
    orders.productCode()
    # orders.productDetails()
    # orders.productPrice()