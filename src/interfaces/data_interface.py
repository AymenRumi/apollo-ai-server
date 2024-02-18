from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def add(self, args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get(self, args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_all(self, args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, args, **kwargs):
        raise NotImplementedError
