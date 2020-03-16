# coding=utf-8
import requests
import json
import os
import root
from project.utils.config_reader import ConfigReader

ConfigReader.read_config()
api = ConfigReader.get_string('server', 'url')

def get_tooken():
    payload ={
        "username": "aam_admin",
        "password": "cofeye11"
    }
    c=requests.Session()
    res=c.post(url = api + '/login_user',data = payload)
    tk=res.cookies.get_dict().get('tms2_9000')
    # c.headers={"cookies":"tms2_9000="+tk}
    # return c.headers
    return tk

def query_pack():

	payload = {
		"sEcho": 1,
		"iColumns": 12,
		"sColumns": "",
		"iDisplayStart": 0,
		"iDisplayLength": 100,
		"mDataProp_0": "uuid",
		"mDataProp_1": "function",
		"mDataProp_2": "function",
		"mDataProp_3": "function",
		"mDataProp_4": "function",
		"mDataProp_5": "function",
		"mDataProp_6": "function",
		"mDataProp_7": "function",
		"mDataProp_8": "function",
		"mDataProp_9": "function",
		"mDataProp_10": "function",
		"mDataProp_11": "function",
		"sSearch": "",
		"bRegex": False,
		"sSearch_0": "",
		"bRegex_0": False,
		"bSearchable_0": True,
		"sSearch_1": "",
		"bRegex_1": False,
		"bSearchable_1": False,
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
		"bSearchable_5": False,
		"sSearch_6": "",
		"bRegex_6": False,
		"bSearchable_6": False,
		"sSearch_7": "",
		"bRegex_7": False,
		"bSearchable_7": False,
		"sSearch_8": "",
		"bRegex_8": False,
		"bSearchable_8": False,
		"sSearch_9": "",
		"bRegex_9": False,
		"bSearchable_9": True,
		"sSearch_10": "",
		"bRegex_10": False,
		"bSearchable_10": True,
		"sSearch_11": "",
		"bRegex_11": False,
		"bSearchable_11": True,
		"iSortCol_0": 3,
		"sSortDir_0": "asc",
		"iSortCol_1": 2,
		"sSortDir_1": "asc",
		"iSortingCols": 2,
		"bSortable_0": False,
		"bSortable_1": False,
		"bSortable_2": True,
		"bSortable_3": True,
		"bSortable_4": True,
		"bSortable_5": False,
		"bSortable_6": True,
		"bSortable_7": True,
		"bSortable_8": False,
		"bSortable_9": True,
		"bSortable_10": True,
		"bSortable_11": False,
		"placeholder_filter": None,
		"screen_number_filter": None,
		"rating_filter": None
	}

	resp = requests.post(api + '/core/paginated/get_datatables_packs', json=payload, cookies=dict(tms2_9000=get_tooken()))

	json_obj = json.loads(resp.content)

	filename = 'write_data.txt'

	with open(root.get_root_path() + '/output/pack_uuid.txt', 'w') as f:
		for data in json_obj['aaData']:
			uuid = data['uuid']
			f.write(uuid + '\n')
