from Educador import Educador
from Estudante import Estudante

class Professor(Estudante, Educador):
    def __init__(self,matricula: int = 0 ,  nome: str = '', idade: int = 0, cargaHoraria: int = 0, salario: float = 0 ):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.cargaHoraria = cargaHoraria
        self.salario = salario
        
    def estudar(self):
        print("Estudando conteúdo novo!")

    def ensinar(self):
        print("Ensinando alunos!")

    def avaliar(self):
        print("Avaliando aluno!")