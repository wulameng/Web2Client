from abc import ABCMeta, abstractmethod


class IMessage(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def attach(self, ob):
        raise NotImplementedError

    @abstractmethod
    def detach(self, ob):
        raise NotImplementedError

    @abstractmethod
    def notify(self, list):
        raise NotImplementedError


class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, list):
        raise NotImplementedError
