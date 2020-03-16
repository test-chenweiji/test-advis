# coding=utf-8
import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation
from project.operation.common.db_query import DBQuery
'''
    初始化POS售票系统 
'''
class InitPOSSystem(RequestOperation):

    # def __init__(self, url):
    #     super().__init__(url)

    def request(self):
        ip = "http://172.22.1.107:29957/TService.asmx"
        manufacturer = "finixx"
        category = "pos"
        if DBQuery.is_exist(
                self._url,
                'Device', "ip = '{}' and type = '{}' and category = '{}' "
                        .format(ip, manufacturer, category), cookies=sw_db.database['cookies']):
            print ('影院设备'+ category + ':' + manufacturer +'已存在,不再新增')
            return
        data = {
            "device": {
                "type": manufacturer,
                "mounted": False,

                "ip": ip,
                "category": category,
                "custom_params": {},
                "dual_mode": False,
                "slave": {
                    "type": "finixx",
                    "mounted": False,
                    "category": "pos",
                    "custom_params": {},
                    "name": "Finixx- Slave"
                }
            }
        }
        resp = requests.post(self._url + '/core/configuration/save_device',
                             json=data,
                             cookies=sw_db.database['cookies'])
        # print(resp.status_code)
        # print(resp.content)
        return resp


