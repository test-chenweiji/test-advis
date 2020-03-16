# coding=utf-8
import requests

import root
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json

class PosMapping(RequestOperation):

    def __init__(self, url):
        super().__init__(url)

    def request(self):
        txt = []
        for line in open(root.get_root_path() + "/output/pos_info.txt", "r"):  # 设置文件对象并读取每一行文件
            txt.append(line)  # 将每一行文件加入到list中
        pos_uuid = txt[0][:36]

        f = open(root.get_root_path() + "/output/playlist_uuid.txt","r")
        datalist = f.readlines()
        playlist_uuid = datalist[0][:36]

        data = {
	"pos_update_map": {
		pos_uuid: {
			"placeholder_type": None,
			"playlist_id": playlist_uuid,
			"show_attributes": {},
			"state": "assigned"
		}
	}
}
        resp = requests.post(self._url + '/core/pos/save_mappings', json = data,cookies=sw_db.database['cookies'])
        return resp
        print(resp.json())




