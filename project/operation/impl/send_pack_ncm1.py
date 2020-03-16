import requests
import uuid
import random
import string
import json
import root
from project.utils.config_reader import ConfigReader

def pack_ncm():
    ConfigReader.read_config()
    advis_url = ConfigReader.get_string('advis', 'advis_url')

    headers = {
        'Content-Type': 'application/json'
    }

    pack_uuid = str(uuid.uuid4())
    screen = random.randint(1, 24)
    pack_name = 'a'.join(random.sample(string.ascii_letters + string.digits, 5))

    f = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist = f.readlines()[1:2]
    screen = datalist[0][:36]
    screen1 = screen.replace('\n', '')

    f1 = open(root.get_root_path() + "/output/pos_info.txt", "r")
    datalist2 = f1.readlines()[2:3]
    start = datalist2[0][:36]
    start1 = start.replace('\n', '')

    payload = {
        "pack": {
            "UUID": pack_uuid,
            "PackName": pack_name,
            "Issuer": "AAM",
            "PlaceholderName": "3D Advertisement",
            "PerformanceDateTime": start1,
            "Screen": screen1,
            "Elements": [
                {
                    "ContentTitleText": "702_AoDi_A6L_30S_jpg239",
                    "UUID": "34a287f6-8597-40df-9764-0ad9e4554b2e",
                    "Duration": 312,
                    "EditRate": "24 1"
                },
                {
                    "ContentTitleText": "PULP-FIC-FTRETTE_SHR_F_EN-XX_INT_20_2K_PRKC_20121227_AAM_OV",
                    "UUID": "45e695fe-30fd-4410-a211-f18a56bf87ac",
                    "Duration": 312,
                    "EditRate": "24 1"
                }
            ]
        }
    }

    resp = requests.post(advis_url + '/v1/pack', headers=headers, json=payload)
    json_obj = json.loads(resp.content)
    pack_uuid = json_obj['UUID']
    with open(root.get_root_path() + '/output/pack_uuid.txt', 'w') as f:
        f.write(pack_uuid + '\n')

