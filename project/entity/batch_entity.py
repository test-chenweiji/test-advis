# coding=utf-8

"""
    针对多服务器批发请求参数封装
"""
import typing


class BatchEntity:

    def __init__(self, server_url: str, port: str, username: str, password: str, params: typing.List[dict], theater_id: str):
        self._server_url = server_url
        self._port = port
        self._username = username
        self._password = password
        self._params = params
        self._theater_id = theater_id

    @property
    def server_url(self) -> str:
        return self._server_url

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def port(self) -> str:
        return self._port

    @property
    def params(self) -> typing.List[dict]:
        return self._params

    @property
    def theater_id(self) -> str:
        return self._theater_id
