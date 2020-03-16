# coding=utf-8
import requests

import root
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json

class CreatePlaylistUuid(RequestOperation):

    def __init__(self, url):
        super().__init__(url)

    def request(self):
        txt = []
        for line in open(root.get_root_path() + "/output/lms_uuid.txt", "r"):  # 设置文件对象并读取每一行文件
            txt.append(line)  # 将每一行文件加入到list中
        device_uuid = txt[0][:36]
        data = {
            "sEcho": 1,
            "iColumns": 10,
            "sColumns": "",
            "iDisplayStart": 0,
            "iDisplayLength": 100,
            "mDataProp_0": "function",
            "mDataProp_1": "function",
            "mDataProp_2": "function",
            "mDataProp_3": "function",
            "mDataProp_4": "function",
            "mDataProp_5": "function",
            "mDataProp_6": "function",
            "mDataProp_7": "function",
            "mDataProp_8": "function",
            "mDataProp_9": "function",
            "sSearch": "",
            "bRegex": False,
            "sSearch_0": "",
            "bRegex_0": False,
            "bSearchable_0": True,
            "sSearch_1": "",
            "bRegex_1": False,
            "bSearchable_1": True,
            "sSearch_2": "",
            "bRegex_2": False,
            "bSearchable_2": True,
            "sSearch_3": "",
            "bRegex_3": False,
            "bSearchable_3": True,
            "sSearch_4": "",
            "bRegex_4": False,
            "bSearchable_4": True,
            "sSearch_5": "",
            "bRegex_5": False,
            "bSearchable_5": True,
            "sSearch_6": "",
            "bRegex_6": False,
            "bSearchable_6": True,
            "sSearch_7": "",
            "bRegex_7": False,
            "bSearchable_7": True,
            "sSearch_8": "",
            "bRegex_8": False,
            "bSearchable_8": True,
            "sSearch_9": "",
            "bRegex_9": False,
            "bSearchable_9": True,
            "iSortCol_0": 3,
            "sSortDir_0": "asc",
            "iSortingCols": 1,
            "bSortable_0": False,
            "bSortable_1": False,
            "bSortable_2": False,
            "bSortable_3": False,
            "bSortable_4": True,
            "bSortable_5": True,
            "bSortable_6": True,
            "bSortable_7": True,
            "bSortable_8": True,
            "bSortable_9": False,
            "device_uuid": device_uuid
    }
        resp = requests.post(self._url + '/core/paginated/get_datatables_playlists', json = data,cookies=sw_db.database['cookies'])
        return resp

    def deal_resp(self, resp):
        if resp.status_code != 200:
            return
        json_obj = json.loads(resp.content)
        with open(root.get_root_path() + '/output/playlist_uuid.txt', 'w') as f:
            for data in json_obj['aaData']:
                uuid = data['uuid']
                #print(uuid)
                f.write(uuid + '\n')


