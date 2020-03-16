# coding=utf-8
import requests
import random
import root
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json

class CreatePlaylist(RequestOperation):

    def __init__(self, url):
        super().__init__(url)

    def request(self):
        txt = []
        for line in open(root.get_root_path() + "/output/lms_uuid.txt", "r"):  # 设置文件对象并读取每一行文件
            txt.append(line)  # 将每一行文件加入到list中
        device_uuid = txt[0][:36]

        f = open(root.get_root_path() + "/output/placeholder_uuid.txt","r")
        datalist = f.readlines()
        placeholder_uuid = datalist[0][:36]

        data = {
	"device_id": device_uuid,
	"playlist": {
		"duration_in_seconds": 2,
		"title": "3d-2",
		"events": [{
			"type": "composition",
			"cpl_id": "ce194f67-92be-4774-b05b-f54ccf62a5f0",
			"duration_in_seconds": 2,
			"duration_in_frames": 48,
			"cpl_start_time_in_seconds": 0,
			"cpl_start_time_in_frames": 0,
			"edit_rate": [24, 1],
			"text": "Content_for_Andy_2s_feature_2k_51",
			"playback_mode": "2D",
			"content_kind": "feature",
			"automation": []
		}, {
			"type": "placeholder",
			"uuid": placeholder_uuid,
			"text": "3D Advertisement",
			"automation": []
		}],
		"is_3d": False,
		"is_hfr": False,
		"is_4k": False,
		"automation": []
	}
}
        resp = requests.post(self._url + '/core/playlist/save', json = data,cookies=sw_db.database['cookies'])
        return resp
        print(resp.json())

    def deal_resp(self, resp):
        if resp.status_code != 200:
            return
        json_obj = json.loads(resp.content)

        with open(root.get_root_path() + '/output/playlist_uuid.txt', 'w') as f:
            for data in json_obj['messages']:
                uuid = data['playlist_uuid']
                f.write(uuid + '\n')


