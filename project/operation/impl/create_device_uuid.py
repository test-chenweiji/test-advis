# coding=utf-8
import requests

import root
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json

class CreateDeviceUuid(RequestOperation):

    def __init__(self, url):
        super().__init__(url)

    def request(self):
        resp = requests.post(self._url + '/core/complex', cookies=sw_db.database['cookies'])
        return resp

    def deal_resp(self, resp):
        if resp.status_code != 200:
            return
        # print(global_val.value)
        # print(resp.content)
        json_obj = json.loads(resp.content)
        with open(root.get_root_path() + '/output/device_uuid.txt', 'w') as f:
            for k in json_obj['data']['status'].keys():
                # print('key: {}'.format(k))
                f.write(k + '\n')


