# coding=utf-8
import typing

from project.entity.batch_entity import BatchEntity
from project.global_value.global_values import device_defaults
from project.operation.base.request_operation_batch import RequestOperationBatch
from project.operation.base.request_operation_batch_multi import RequestOperationBatchMulti
from device_init.init_device_batch2 import InitDeviceBatch2
import pandas as pd

"""
    批初始化多个服务器上的设备
"""
class InitDeviceBatchMulti2(RequestOperationBatchMulti):

    # CONVERT_TABLE = {
    #     'Projector': 'projector',
    #     'Media Block': 'sms',
    #     'SMS': 'sms',
    #     None: None
    # }

    def __init__(self, cvs_path, entity_list: typing.List[BatchEntity] = None):
        super().__init__(entity_list)
        self._cvs_path = cvs_path
        self._other = {}

    def _get_request_operation_batch(self) -> type(RequestOperationBatch):
        return InitDeviceBatch

    def pre_request(self):
        # 读取数据
        df = pd.read_csv(self._cvs_path, header=1)
        init_df = df.fillna('')
        temp_map = self._make_params(init_df)
        temp_u_map = self._make_u_params(init_df)
        entity_list = self._merge_params(temp_map, temp_u_map)
        self.entity_list = entity_list

    """
        生成参数数组temp_list
    """
    def _make_params(self, df: pd.DataFrame):
        temp_map = {}
        for index, row in df.iterrows():
            theater_id = str(row["Theater ID"])
            category = self.CONVERT_TABLE[row['Equipment Category']]    # projector等, 需要转小写, 某些还要转换名称
            manufacturer = row['Manufacturer'].lower()                  # Sony等, 需要转小写
            ip = row['Management IP Address']                           # IP直接用

            json = {
                'device': {
                    'category': category,
                    'custom_params': {},
                    'dual_mode': False,
                    # 'enabled': True,
                    'ip': ip,
                    # 'is_master': True,
                    'mounted': False,
                    # 在batch层添加此uuid
                    # 'screen_uuid': screen_uuid,
                    'slave': {
                        'category': category,
                        'custom_params': {},
                        'mounted': False,
                        'name': '{}- Slave'.format(row['Manufacturer']),
                        'type': manufacturer,
                        # 在batch层添加此uuid
                        # 'screen_uuid': screen_uuid
                    },
                    'type': manufacturer
                    # 'uuid': None            # 如果是更新,需要加上uuid
                }
            }

            if 'api_username' in device_defaults[category][manufacturer]:
                json['device']['api_username'] = device_defaults[category][manufacturer]['api_username']
            if 'api_password' in device_defaults[category][manufacturer]:
                json['device']['api_password'] = device_defaults[category][manufacturer]['api_password']
            if 'port' in device_defaults[category][manufacturer]:
                json['device']['port'] = device_defaults[category][manufacturer]['port']
            if 'ftp_port' in device_defaults[category][manufacturer]:
                json['device']['ftp_port'] = device_defaults[category][manufacturer]['ftp_port']
            if 'ftp_username' in device_defaults[category][manufacturer]:
                json['device']['ftp_username'] = device_defaults[category][manufacturer]['ftp_username']
            if 'ftp_password' in device_defaults[category][manufacturer]:
                json['device']['ftp_password'] = device_defaults[category][manufacturer]['ftp_password']
            if row['Content IP Address'] != 'nan' and row['Content IP Address'] != '':
                json['device']['ftp_ip'] = row['Content IP Address']

            if theater_id not in temp_map:
                temp_map[theater_id] = []
            temp_map[theater_id].append(json)
        return temp_map

    """
        生成唯一参数
        :return key为影院id, value为影院登录所需要的数据{TmsIP,UserName,PassWord}
    """
    def _make_u_params(self, df: pd.DataFrame):
        temp_u_map = {}
        for index, row in df.iterrows():
            theater_id = str(row['Theater ID'])
            if theater_id not in temp_u_map:
                temp_u_map[theater_id] = {
                    'TmsIP': '',
                    'UserName': '',
                    'PassWord': '',
                }

            if row['TmsIP'] != 'nan' and row['TmsIP'] != '':
                temp_u_map[theater_id]['TmsIP'] = row['TmsIP']
            if row['UserName'] != 'nan' and row['UserName'] != '':
                temp_u_map[theater_id]['UserName'] = row['UserName']
            if row['PassWord'] != 'nan' and row['PassWord'] != '':
                temp_u_map[theater_id]['PassWord'] = row['PassWord']
            # if row['Content IP Address'] != 'nan' or row['Content IP Address'] != '':
            #     res_map[theater_id]['Content IP Address'] = row['Content IP Address']
        return temp_u_map

    """
        合并参数
    """
    @staticmethod
    def _merge_params(temp_map, temp_u_map):
        entity_list = []
        for key in temp_u_map:
            entity = BatchEntity(temp_u_map[key]['TmsIP'],
                                 '9000',
                                 temp_u_map[key]['UserName'],
                                 temp_u_map[key]['PassWord'],
                                 temp_map[key],
                                 key)
            entity_list.append(entity)
        return entity_list
