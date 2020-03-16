# coding=utf-8
import requests

import root
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json

class GetLmsUuid(RequestOperation):

    def __init__(self, url):
        super().__init__(url)

    def request(self):
        resp = requests.post(self._url + '/core/device_infos', cookies=sw_db.database['cookies'])
        return resp

    def deal_resp(self, resp):
        if resp.status_code != 200:
            return
        json_obj = json.loads(resp.content)
        with open(root.get_root_path() + '/output/lms_uuid.txt', 'w') as f:
            for k,v in json_obj['data']['devices'].items():
                if v["category"].lower()=='lms':
                    f.write(k + '\n')



