from abc import ABC, abstractmethod

class Crud(ABC):
    def __init__(self):
        self.data = []
    @abstractmethod
    def criar(self):
        pass
    
    @abstractmethod
    def editar(self,id):
        pass
    
    @abstractmethod
    def ver(self):
        pass
    
    @abstractmethod
    def excluir(self,id):
        pass
    

