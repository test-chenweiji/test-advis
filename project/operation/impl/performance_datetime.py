import requests
import root
import logging
from project.utils.config_reader import ConfigReader
import datetime
from project.operation.impl.schedule_validate import schedule_validate

def  performance():
    ConfigReader.read_config()
    advis_url = ConfigReader.get_string('advis', 'advis_url')

    f = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist = f.readlines()[1:2]
    screen = datalist[0][:36]
    screen1 = screen.replace('\n', '')

    f1 = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist2 = f1.readlines()[2:3]
    start = datalist2[0][:36]
    start1 = start.replace('\n', '')
    start2 = start1.replace('T',' ')

    source_start = datetime.datetime.strptime(start2, "%Y-%m-%d %H:%M:%S")
    now_time = datetime.datetime.now()

    f2 = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist3 = f2.readlines()[4:5]
    feature_title = datalist3[0][:36]
    feature_title1 = feature_title.replace('\n', '')

    url = advis_url + "/v1/performance-status?screen=%s&performance_datetime=%s"%(screen1,start1)
    not_find_str = screen1 + "号厅" + feature_title1 + '影片在' + start1 + '场次未找到对应占位符匹配的内容包'
    find_str = screen1 + "号厅" + feature_title1 + '影片在' + start1 + '场次已添加对应占位符匹配的内容包CPL'
    resp = requests.request("GET", url)
    resp2 = resp.json()
    if (resp2.get('Packs')):
        return find_str
    else:
        if (source_start - now_time) < datetime.timedelta(hours=2):
            if schedule_validate():
                return find_str + '（保护场次）'

            else:
               return not_find_str

        else:
           return not_find_str



