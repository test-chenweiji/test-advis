# coding=utf-8
import requests

import root
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json

class GetPlaceholderUuid(RequestOperation):

    def __init__(self, url):
        super().__init__(url)

    def request(self):
        data = {
	"sorted_list": True
}
        resp = requests.post(self._url + '/core/placeholder/placeholders',json = data, cookies=sw_db.database['cookies'])
        return resp

    def deal_resp(self, resp):
        if resp.status_code != 200:
            return
        json_obj = json.loads(resp.content)


        with open(root.get_root_path() + '/output/placeholder_uuid.txt', 'w') as f:
            for data in json_obj['data']:
                if (data['name'] == '3D Advertisement'):
                    uuid = data['uuid']
                    f.write(uuid + '\n')



