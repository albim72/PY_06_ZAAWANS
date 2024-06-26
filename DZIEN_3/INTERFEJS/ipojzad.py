from abc import ABCMeta, abstractmethod
class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie(self,odl,jedn):raise NotImplementedError

    @abstractmethod
    def kosztyprzejzadu(self,odl,jedn,cenaj):raise NotImplementedError
