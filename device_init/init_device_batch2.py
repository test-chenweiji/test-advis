# coding=utf-8
from functools import reduce

from project.exception.db_query_exception import DBQueryException
from project.operation.base.request_operation import RequestOperation
from project.operation.base.request_operation_batch import RequestOperationBatch
from project.operation.common.db_query import DBQuery
from device_init.init_device import InitDevice
from device_init.create_screen import CreateScreen


class InitDeviceBatch2(RequestOperationBatch):

    def __init__(self, url, data_tuple: tuple = None, force_exc=True, **other):
        super().__init__(url, data_tuple, force_exc, **other)

    def _get_request_operation(self) -> type(RequestOperation):
        return InitDevice

    def pre_request(self):
        cookies = self._other['cookies']
        res = None
        try:
            res = DBQuery.query_list(self._url, 'Screen', None, limit=150, cookies=cookies)
        except DBQueryException as e:
            print('数据库查询异常，忽略此次批处理')
            return
        except Exception as e:
            print('数据库查询出现异常:{}，忽略此次批处理'.format(e))

        if res is None:
            print('url:{}, 找不到影厅列表'.format(self._url))
            return

        def add(acc, item):
            acc[item['identifier']] = item['uuid']
            return acc
        # 厅号对应的uuid key:厅号, value:uuid
        device_mapper = reduce(add, res, {})

        new_data_tuple = []
        for item in self._data_tuple:
            # aud_num = item['aud_num']
            # if aud_num not in device_mapper:
            #     print('影厅编号:{}不存在于当前系统, 尝试添加该影厅...'.format(aud_num))
            #     # 尝试添加影厅
            #     screen_uuid = CreateScreen(self._url, aud_num, aud_num, cookies=cookies).execute()
            #     if screen_uuid is None:
            #         print('影厅编号:{}添加失败, 忽略此次添加'.format(aud_num))
            #         continue
            #     print(f'影厅添加成功, uuid:{screen_uuid}')
            #     device_mapper[aud_num] = screen_uuid
            # else:
            #     screen_uuid = device_mapper[aud_num]

            manufacturer = item['device']['type']
            category = item['device']['category']
            try:
                if DBQuery.is_exist(
                        self._url,
                        'Device', "type = '{}' and category = '{}'"
                                .format( manufacturer, category), cookies=cookies):
                    print('设备:{} 已存在,不作新增'.format(category))
                    continue
            except DBQueryException as e:
                print('设备:{}, 发生DBQueryException:{}, 不作新增'.format(category, e))
                continue
            except Exception as e:
                print('数据库查询出现异常:{}，忽略此次批处理'.format(e))

            data = item['device']
            new_data_tuple.append({'device': data})
        self._data_tuple = new_data_tuple
        # print(self._data_tuple)

