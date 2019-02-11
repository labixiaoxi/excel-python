import time,datetime
class InsuranceTime:
    def nowtime(self):
        nowtime=datetime.date.today()
        return nowtime

    def policyBeginDate(self,day):
        return str(self.nowtime()+datetime.timedelta(days=day))+" 00:00:00"

    def policyEndDate(self,day):
        return str(self.nowtime()+datetime.timedelta(days=day))+" 23:59:59"


if __name__ == '__main__':
    policyDate=InsuranceTime()
    print policyDate.nowtime()
    print policyDate.policyBeginDate(1)
    print policyDate.policyEndDate(365)