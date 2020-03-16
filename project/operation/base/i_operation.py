# coding=utf-8

from abc import ABCMeta, abstractmethod, abstractproperty


class IOperation(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        raise Exception('This method must be implemented in subclasses')
