# coding=utf-8
import requests

from project.operation.base.request_operation import RequestOperation
from project.database import sw_db
import json


class CreateScreen(RequestOperation):

    def __init__(self, url, identifier, title, **other):
        super().__init__(url, **other)
        self._data = {
            'screens': [
                {
                    'identifier': identifier,
                    'title': title,
                    'capabilities': [],
                    'show_attributes': []
                }
            ]
        }

    def request(self):
        resp = requests.post(self._url + '/core/configuration/save_screen', json=self._data, cookies=self._other['cookies'])
        return resp

    def deal_resp(self, resp):
        if resp.status_code != 200:
            return
        # {
        # "messages":[{"message":"\u5df2\u4fdd\u5b58\uff1a10","type":"success"}],
        # "data":{"uuid":"214f29e0-dad8-42a2-a0aa-6c54f6e2c5a2"}
        # }
        json_obj = json.loads(resp.content)
        if json_obj['messages'][0]['type'] == 'success':
            return json_obj['data']['uuid']
        return


