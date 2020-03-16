# coding=utf-8
import typing

import requests

from project.entity.batch_entity import BatchEntity
from project.exception.login_exception import LoginException
from project.operation.base.i_operation import IOperation
from project.operation.base.no_request_operation_batch import NoRequestOperationBatch
from project.operation.base.request_operation_batch import RequestOperationBatch

"""
    针对多服务器批发请求

"""
class RequestOperationBatchMulti(IOperation):

    def __init__(self, entity_list: typing.List[BatchEntity]=None):
        if entity_list is None:
            entity_list = []
        self._entity_list = entity_list
        self._operation_batch = self._get_request_operation_batch()

    @property
    def entity_list(self):
        return self._entity_list

    @entity_list.setter
    def entity_list(self, v_list: typing.List[BatchEntity]):
        self._entity_list = v_list

    def _get_request_operation_batch(self) -> type(RequestOperationBatch):
        return NoRequestOperationBatch

    def pre_request(self):
        pass

    def execute(self):
        self.pre_request()
        # 每个entity对应一台应用服务器
        for entity in self.entity_list:
            print('开始对服务器:{}进行批处理'.format(entity.server_url))
            server = entity.server_url
            username = entity.username
            password = entity.password
            port = entity.port
            params = entity.params
            theater_id = entity.theater_id
            if len(server) == 0 or len(username) == 0 or len(password) == 0:
                print('影院ID: {} .server:{}, username:{}, password:{}, 其中一个为空, 忽略此服务器初始化操作'.format(
                    theater_id, server, username, password
                ))
                continue

            try:
                cookies = self._login(server, port, username, password, theater_id)
            except LoginException as e:
                print('服务器登录失败, username:{}, password:{}, 忽略对当前影院ID {} 的初始化'.format(username, password, theater_id))
                continue

            # 执行批处理
            self._operation_batch('http://{}:{}'.format(server, port), data_tuple=params, **{'cookies': cookies}).execute()
            print('对服务器:{}批处理完毕'.format(entity.server_url))

        self.post_request()

    def post_request(self):
        pass

    @staticmethod
    def _login(server, port, username, password, theater_id):
        resp = None
        try:
            resp = requests.post('http://{}:{}/login_user'.format(server, port),
                             data={'username': username, 'password': password})
        except Exception as e:
            raise LoginException('影院ID:{} 登录连接异常:{}'.format(theater_id, e))

        # print(resp.content)
        # print(resp.cookies)
        return resp.cookies
