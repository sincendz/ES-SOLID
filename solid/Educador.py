from abc import ABC, abstractmethod

class Educador(ABC):
    @abstractmethod
    def ensinar(self):
        pass
    
    @abstractmethod
    def avaliar(self):
        pass