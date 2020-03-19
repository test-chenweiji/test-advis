# coding=utf-8
import sys
import os
import uuid
import psycopg2
import time
import root
import datetime
from project.utils.config_reader import ConfigReader

ConfigReader.read_config()
host = ConfigReader.get_string('database', 'host')
port = ConfigReader.get_string('database','port')

connent = psycopg2.connect(database="tms2", user="postgres", password="postgres",
                           host=host, port=port)
cursor = connent.cursor()

def query_pos():
    time1 = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    source_start = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    source_start2 = source_start + datetime.timedelta(days = 14)
    time2 = datetime.datetime.strftime(source_start2, "%Y-%m-%d %H:%M:%S")

    cursor.execute("SELECT pos.uuid,pos.screen_identifier,pos.source_start,pos.feature_id,pos.feature_title,external_device_map.device_uuid FROM pos JOIN external_device_map ON pos.screen_identifier=external_device_map.external_id WHERE source_start > '%s' AND source_start < '%s' " % (time1,time2))
    result = cursor.fetchone()
    if result:
        pos_uuid = result[0]
        screen = result[1]
        for k, i in enumerate(screen):
            if i != '0':
                _screen = screen[k:]
                break
        source_start = result[2]
        start = str(source_start)
        start = start.replace(' ', 'T')
        feature_id = result[3]
        feature_title = result[4]
        device_uuid = result[5]

        with open(root.get_root_path() + '/output/pos_info.txt', 'w') as f:
            f.write(pos_uuid + '\n')
            f.write(_screen + '\n')
            f.write(start + '\n')
            f.write(feature_id + '\n')
            f.write(feature_title + '\n')
            f.write(device_uuid + '\n')

    else:
        print ('数据库查询POS数据为空或POS数据已过期，请添加POS后再运行')
        input('输入任意键退出...')
        sys.exit(0)


    connent.commit()
    connent.close()
