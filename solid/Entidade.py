from abc import ABC, abstractmethod

class Entidade(ABC):
    @abstractmethod
    def __str__(self):
        pass