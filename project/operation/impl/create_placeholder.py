# coding=utf-8
import requests

from project.database import sw_db
from project.operation.base.request_operation import RequestOperation

'''
    创建3D Advertisement占位符
'''
class Create_Placeholder(RequestOperation):

    # def __init__(self, url):
    #     super().__init__(url)

    def request(self):
        data = {
	"placeholders": [{
		"name": "3D Advertisement",
		"warn": True
	}]
}
        resp = requests.post(self._url + '/core/placeholder/save',
                             json=data,
                             cookies=sw_db.database['cookies'])
        # print(resp.status_code)
        # print(resp.content)
        return resp
