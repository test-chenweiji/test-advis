import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation

'''
    初始化Advanced  spl 开关
'''
class InitAdvancedSpl(RequestOperation):

    # def __init__(self, url):
    #     super().__init__(url)

    def request(self):
        data = {
            "configs": {
                "pos_spl_mapping_enabled": True
            }
        }
        resp = requests.post(self._url + '/core/configuration/set_configuration',
                             json=data,
                             cookies=sw_db.database['cookies'])
        # print(resp.status_code)
        # print(resp.content)
        return resp
