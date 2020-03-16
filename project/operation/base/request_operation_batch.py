# coding=utf-8
from project.global_value.global_values import global_values
from project.operation.base.i_operation import IOperation

from project.operation.base.no_request_operation import NoRequestOperation
from project.operation.base.request_operation import RequestOperation


class RequestOperationBatch(IOperation):

    def __init__(self, url, data_tuple: tuple=None, force_exc=True, **other):
        self._url = url
        self._data_tuple = data_tuple
        self._force_exc = force_exc
        self._operation = self._get_request_operation()
        self._other = other

    def _get_request_operation(self) -> type(RequestOperation):
        return NoRequestOperation

    def pre_request(self):
        pass

    def execute(self):
        self.pre_request()
        global_values['index'] = 0
        if self._data_tuple is not None:
            for item in self._data_tuple:
                self._operation(self._url, data=item, **self._other).execute()
                global_values['index'] += 1
                # print(global_values['index'])
        elif self._force_exc:
            self._operation(self._url).execute()
        self.post_request()

    def post_request(self):
        pass
