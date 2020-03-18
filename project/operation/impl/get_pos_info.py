# coding=utf-8
import sys
import os
import uuid
import psycopg2
import time
import root
from project.utils.config_reader import ConfigReader

ConfigReader.read_config()
host = ConfigReader.get_string('database', 'host')
port = ConfigReader.get_string('database','port')

connent = psycopg2.connect(database="tms2", user="postgres", password="postgres",
                           host=host, port=port)
cursor = connent.cursor()

def query_pos():
    time1 = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    cursor.execute("SELECT uuid,screen_identifier,source_start,feature_id,feature_title FROM pos where source_start > '%s'" % time1)
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

        with open(root.get_root_path() + '/output/pos_info.txt', 'w') as f:
            f.write(pos_uuid + '\n')
            f.write(_screen + '\n')
            f.write(start + '\n')
            f.write(feature_id + '\n')
            f.write(feature_title + '\n')

    else:
        print ('数据库查询POS数据为空或POS数据已过期，请添加POS后再运行')
        sys.exit(0)


    connent.commit()
    connent.close()
