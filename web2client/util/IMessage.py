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
    def notify(self, *args):
        raise NotImplementedError


class Observer(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args):
        raise NotImplementedError
