# coding=utf-8

from project.operation.base.request_operation import RequestOperation

'''
    请求空对象
'''
class NoRequestOperation(RequestOperation):

    def request(self):
        print("warning: 没有方法执行!!")
        pass
