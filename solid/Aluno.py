from Estudante import Estudante

class Aluno(Estudante):
    def __init__(self,id: int = 0, nome: str = '', idade: int = 0, curso: str = '' ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso
    def estudar(self):
        print("Estudando!")
    