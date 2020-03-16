# coding=utf-8
from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import requests


class Login(RequestOperation):

    def __init__(self, url, username, password):
        super().__init__(url)
        self.__username = username
        self.__password = password

    def pre_request(self):
        self._data = {'username': self.__username, 'password': self.__password}
        #self._data = {'IP:': self.__url}

    def request(self):
        resp = requests.post(self._url + '/login_user', data=self._data)
        return resp

    def deal_resp(self, resp):
        sw_db.database['cookies'] = resp.cookies
