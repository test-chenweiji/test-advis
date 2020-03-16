# coding=utf-8
import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation

'''
    初始化传输设置
'''
class InitPOSSetting(RequestOperation):

    # def __init__(self, url):
    #     super().__init__(url)

    def request(self):
        data = {
             "pos_config": {
            "pos_feed_type": "",
            "pos_week_offset": "0",
            "pos_first_day_of_week": "0",
            "pos_cinema_identifier": "42103201",
            "pos_default_session_length": "120",
            "pos_enabled": True,
            "pos_auto_transfer_time": True,
            "pos_auto_map_templates": False,
            "pos_strict_template_matching": False,
            "pos_lms_auto_sync": False,
            "pos_spl_mapping_enabled": True
             }
        }
        resp = requests.post(self._url + '/core/pos/set_configuration',
                             json=data,
                             cookies=sw_db.database['cookies'])
        # print(resp.status_code)
        # print(resp.content)
        return resp
