# coding=utf-8
#coding:utf-8
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
    cursor.execute("SELECT uuid,screen_identifier,source_start,feature_id FROM pos where source_start > '%s'" % time1)
    result = cursor.fetchone()
    pos_uuid = result[0]
    screen = result[1]
    screen1 = screen.replace('0', '')

    source_start = result[2]
    start = str(source_start)
    start = start.replace(' ', 'T')
    feature_id = result[3]

    with open(root.get_root_path() + '/output/pos_info.txt', 'w') as f:
        f.write(pos_uuid + '\n')
        f.write(screen1 + '\n')
        f.write(start + '\n')
        f.write(feature_id + '\n')

    connent.commit()
    connent.close()








