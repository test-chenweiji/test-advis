# coding=utf-8
from project.operation.base.request_operation import RequestOperation
from project.operation.base.request_operation_batch import RequestOperationBatch

'''
    批量请求空对象
'''
class NoRequestOperationBatch(RequestOperationBatch):

    def request(self):
        print("warning: 没有批量方法执行!!")
        pass
