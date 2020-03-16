# coding=utf-8
from functools import reduce

import requests

import root
from project.database import sw_db
from project.global_value.global_values import device_defaults
from project.operation.base.request_operation import RequestOperation
from project.operation.common.db_query import DBQuery

"""
    初始化设备
"""


class InitDevice(RequestOperation):

    def request(self):
        # print(self._other)
        # return
        # print('params:{}'.format(self._data))
        # print(self._other)
        # print(self._other['TmsIP'])

        return requests.post(self._url + '/core/configuration/save_device', json=self._data, cookies=self._other['cookies'])


