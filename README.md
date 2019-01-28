##环境:
window

python 2.7.12

##目录:
--config					数据

	--case.xls              excel管理数据 

	--orderParameter.yaml   部分参数存放在yaml文件

--insurance               

	--insuranceLoginCookies 获取openid,token,cookies

	--insuranceOpera        获取excel每一行的值

	--insuranceParameter    获取接口的部分参数,写入excel

	--insuranceTime         根据参数获取开始时间和结束时间

--logs						日志
	
--public

	--publicDingDing		接口失败,发送到钉钉  
 
	--publicExcel           读取excel方法

	--publicLogs            日志

	--publicMd5             md5加密

	--publicYaml            获取yaml文件方法

--run

	--run					运行的总方法

	--runMain				请求方法的封装

	--runOrders				订单接口的所有参数封装请求
