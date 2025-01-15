from abc import ABC, abstractmethod

class Entidade(ABC):
    @abstractmethod
    #Qualquer classe que herda de entidade implementa o __str__
    #__str__ serve para printar printar o objeto
    def __str__(self):
        pass