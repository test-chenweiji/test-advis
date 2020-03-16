# coding=utf-8
import requests
import json
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

def delete_pack():
    headers = {
        'Content-Type': 'application/json'
    }

    f = open(root.get_root_path() + "/output/pack_uuid.txt", "r")
    a = list(f)
    a1 = [x.strip() for x in a if x.strip() != ""]

    payload = {
        "pack_uuids": a1
    }

    resp = requests.post(api + '/core/pack/delete', json=payload, cookies=dict(tms2_9000=get_tooken()))


