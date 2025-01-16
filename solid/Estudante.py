from abc import ABC, abstractmethod

class Estudante(ABC):
    @abstractmethod
    def estudar(self):
        pass