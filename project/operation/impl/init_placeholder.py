# coding=utf-8
import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation

'''
    初始化占位符
'''
class InitPlaceholder(RequestOperation):

    def __init__(self, url, new_placeholder_list):
        super().__init__(url)
        self.__new_placeholder_list = new_placeholder_list
        self._data = {
            "placeholders": [
                {
                    "name": p,
                    "warn": True
                } for p in self.__new_placeholder_list
            ]
        }


    def request(self):
        resp1 = requests.post(self._url + '/core/placeholder/save',
                             json=self._data,
                             cookies=sw_db.database['cookies'])
        return resp1
