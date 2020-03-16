import requests
import root
from project.utils.config_reader import ConfigReader

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

    url = advis_url + "/v1/performance-status?screen=%s&performance_datetime=%s"%(screen1,start1)

    resp = requests.request("GET", url)
    resp2 = resp.json()
    if (resp2.get('Packs')):
        print (resp2.get('Screen') + '号厅' + resp2.get('POSFilmTitle') + '影片在' + resp2.get(
            'PerformanceDateTime') + '场次已添加对应占位符匹配的内容包CPL')
    else:
        print (resp2.get('Screen') + '号厅' + resp2.get('POSFilmTitle') + '影片在' + resp2.get(
            'PerformanceDateTime') + '场次未找到对应占位符匹配的内容包')







