# *_*coding:utf-8 *_* 
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from public.publicExcel import PublicExcel
class InsuranceOpera(object):
    """
    读取excel所有字段值
    """
    def __init__(self,path):
        self.excel = PublicExcel(path)

    # 产品名称
    def get_productName(self,row):
        read_productName =self.excel.get_value(0,row,1)
        return read_productName

    #产品代号
    def get_productCode(self,row):
        read_productCode = self.excel.get_value(0,row,2)
        return read_productCode

    #保障期间
    def get_productValue(self,row):
        read_productValue  = self.excel.get_value(0,row,3)
        return read_productValue

    #保障类型
    def get_productType(self,row):
        read_productType = self.excel.get_value(0,row,4)
        return read_productType

    #金额
    def get_productPrice(self,row):
        read_productPrice = self.excel.get_value(0,row,5)
        return read_productPrice

    #产品保额
    def get_productPlanName(self,row):
        read_productPlanName = self.excel.get_value(0,row,6)
        return read_productPlanName

    #health
    def get_productHealth(self,row):
        read_productHealth = self.excel.get_value(0,row,7)
        return read_productHealth

    #是否运行
    def get_productRun(self,row):
        read_productRun = self.excel.get_value(0,row,8)
        return read_productRun

    #url
    def get_productUrl(self,row):
        read_productUrl = self.excel.get_value(0,row,9)
        return read_productUrl

    #请求类型
    def get_productRequest(self,row):
        read_productRequest = self.excel.get_value(0,row,10)
        return read_productRequest

    #预期结果
    def get_productExpect(self,row):
        read_productExpect = self.excel.get_value(0,row,11)
        return read_productExpect

    #实际结果
    def get_productActual(self,row):
        read_productActual = self.excel.get_value(0,row,12)
        return read_productActual

    #响应时间
    def get_productTime(self,row):
        read_productTime = self.excel.get_value(0,row,13)
        return read_productTime

    # 写入结果(fail or pass)
    def get_productResult(self,row):
        read_productResult = self.excel.get_value(0,row,14)
        return read_productResult

if __name__ == '__main__':
    path = '../config/case.xls'
    opera = InsuranceOpera(path)
    for i in range(40):
        print opera.get_productValue(i)