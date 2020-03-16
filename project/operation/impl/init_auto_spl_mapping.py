# coding=utf-8

import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation
from project.operation.common.db_query import DBQuery
import root

'''
    初始化自动排期
'''
class InitAutoSplMapping(RequestOperation):


    def __init__(self, url, feature):
        super().__init__(url)
        self.feature = feature['feature']


    def request(self):
        #feature_id = '00110492201701'
        #feature_title = "老兽"
        # state = assigned'
        # if DBQuery.is_exist(
        #         self._url,
        #         'Pos', "state = '{}'".format(state), cookies=sw_db.database['cookies']):
        #     #print ('正片:' + feature_id + '已匹配播放列表')
        #     return
        #
        screen_list = DBQuery.query_list(self._url, 'Screen', None, limit=250)
        if screen_list is None or len(screen_list) == 0:
            print('找不到screen_list')


        data = []
        for screen in screen_list:
            screen_uuid = screen['uuid']
            txt = []
            for line in open(root.get_root_path() + "/output/playlist_uuid.txt", "r"):  # 设置文件对象并读取每一行文件
                txt.append(line)  # 将每一行文件加入到list中
            playlist_uuid = txt[0][:36]
            print (playlist_uuid)
            data.append(
                {
                    "feature_id": self.feature['feature_id'],
                    "playlist_uuid": playlist_uuid,
                    "screen_uuid": screen_uuid,
                    "feature_title": self.feature['feature_title']
                }
            )
        _JSON = {
            'schedule_update_map': data
        }



        resp = requests.post(self._url + '/core/playlist/save_spl_mappings',
                             json=_JSON,
                             cookies=sw_db.database['cookies'])
        return resp
