# coding=utf-8
import json

import requests

from project.database import sw_db
from project.exception.db_query_exception import DBQueryException

class DBQuery:

    @staticmethod
    def query_list(server_url, table, sSearch, limit=10, cookies=None):
        resp = DBQuery.__base_request(server_url, table, sSearch, limit=limit, cookies=cookies)
        return DBQuery.__extract(resp)

    @staticmethod
    def query_one(server_url, table, sSearch, cookies=None):
        resp = DBQuery.__base_request(server_url, table, sSearch, limit=1, cookies=cookies)
        res_list = DBQuery.__extract(resp)
        if (not isinstance(res_list, list)) or len(res_list) == 0:
            return None
        return res_list[0]

    @staticmethod
    def is_exist(server_url, table, sSearch, cookies=None):
        resp = DBQuery.__base_request(server_url, table, sSearch, cookies=cookies)
        res_list = DBQuery.__extract(resp)
        return len(res_list) > 0

    @staticmethod
    def __base_request(server_url, table, sSearch, limit=10, cookies=None):
        if cookies is None:
            cookies = sw_db.database['cookies']
        return requests.post(server_url + '/core/paginated/get_datatables_db',
                      json={
                            "db_model_name": table,
                            "db_name": "primary",
                            "sSearch": sSearch,
                            'iDisplayStart': 0,
                            'iDisplayLength': limit
                        },
                      cookies=cookies)

    @staticmethod
    def __extract(resp, limit=None):
        if resp.status_code != 200:
            raise DBQueryException('抛出DBQuery数据库查询异常 server:{}, code:{}'.format(resp.url
                                                                                        , resp.status_code))
        json_obj = json.loads(resp.content)
        return json_obj['aaData']

