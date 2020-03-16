import requests
import root
from project.utils.config_reader import ConfigReader

def delete_pack2():
    ConfigReader.read_config()
    advis_url = ConfigReader.get_string('advis', 'advis_url')
    f = open(root.get_root_path() + "/output/pack_uuid.txt", "r")
    datalist = f.readlines()
    pack_uuid = datalist[0][:36]

    resp = requests.request("DELETE", advis_url + '/v1/pack/' + pack_uuid)



