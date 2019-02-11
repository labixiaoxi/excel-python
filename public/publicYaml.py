# *_*coding:utf-8 *_* 
import yaml
import os,yaml
class PublicGetYaml:
    def __init__(self,yaml_path):
        self.yaml_path=yaml_path

    def get_Yaml(self):
        try:
            with open(self.yaml_path,'r') as f:
                data=f.read()
                result=yaml.load(data)
                f.close()
                return result
        except Exception:
            return u"未找到yaml文件"

if __name__ == '__main__':
    yaml_path = '../config/orderParameter.yaml'
    getYaml = PublicGetYaml(yaml_path)
    print getYaml.get_Yaml()['caseOrders']['uri']