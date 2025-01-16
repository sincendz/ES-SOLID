from abc import ABC, abstractmethod

# Interface única para todos
class Pessoa(ABC):
    @abstractmethod
    def estudar(self):
        pass
    
    @abstractmethod
    def ensinar(self):
        pass

    @abstractmethod
    def avaliar(self):
        pass 