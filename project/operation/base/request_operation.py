# coding=utf-8
import traceback

from project.exception.db_query_exception import DBQueryException
from project.operation.base.i_operation import IOperation
from abc import abstractmethod



class RequestOperation(IOperation):

    def __init__(self, url, data=None, **other):
        self._url = url
        self._data = data
        self._other = other

    def execute(self):
        self.pre_request()
        try:
            from project.operation.impl.login import Login
            if not isinstance(self,Login):
                print("正在执行:{}, 参数:{}".format(type(self), self._data))
            resp = self.request()
            if resp is not None:
                # if resp.status_code == 200:
                print("返回码:{}, 内容:{}....".format(resp.status_code, resp.text[:1024]))
                # else:
                #     print("返回码:{}, 内容:{}....".format(resp.status_code, resp.text))
                return self.deal_resp(resp)
        except DBQueryException as e:
            print('捕获数据库查询异常: e:{}, method:{}, params'.format(e, self._data))
        except Exception as e:
            print(traceback.print_exc())

    def pre_request(self):
        pass

    @abstractmethod
    def request(self):
        pass

    def deal_resp(self, resp):
        pass
