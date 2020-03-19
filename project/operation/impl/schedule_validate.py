# coding=utf-8
import requests
import json
import root
import datetime
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


def schedule_validate():
    f = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist = f.readlines()[5:6]
    device_uuid = datalist[0][:36]
    device_uuid1 = device_uuid.replace('\n', '')

    f1 = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist2 = f1.readlines()[2:3]
    start = datalist2[0][:36]
    start1 = start.replace('\n', '')
    start2 = start1.replace('T', ' ')
    source_start = datetime.datetime.strptime(start2, "%Y-%m-%d %H:%M:%S")
    start_datetime = source_start - datetime.timedelta(minutes=3)
    start_datetime1 = datetime.datetime.strftime(start_datetime, "%Y-%m-%d %H:%M:%S")
    end_datetime = source_start + datetime.timedelta(minutes=3)
    end_datetime1 = datetime.datetime.strftime(end_datetime, "%Y-%m-%d %H:%M:%S")


    payload = {
	"start_time": start_datetime1,
	"end_time": end_datetime1,
	"device_uuids": [
        device_uuid1
    ]
}

    resp = requests.post(api + '/core/scheduling/schedule', json=payload, cookies=dict(tms2_9000=get_tooken()))
    json_obj = json.loads(resp.content)
    a = None
    templating_issues = []
    for k, v in json_obj['data'].items():
        templating_issues = v.get('templating_issues')
        if not templating_issues:
            a = False
            continue
        else:
            a = True
            break
    if a:
        if templating_issues[0].get('pack_uuid'):
            return True
    else:
        return False





