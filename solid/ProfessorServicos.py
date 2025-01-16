from Professor import Professor
from LerProfessorTerminal import LerProfessorTerminal
from Crud import Crud


class ProfessorServicos(Crud):
    def __init__(self):
        super().__init__()
        self.lerProfessorTerminal = LerProfessorTerminal()

    
    def criar(self):
        matricula,nome,idade,cargaHoraria, salario = self.lerProfessorTerminal.obterDados()
        professor = Professor(matricula,nome,idade,cargaHoraria, salario)
        self.data.append(professor)
        print("professor Adicionado!")
    
    def ver(self):
        if(len(self.data) == 0):
            print("Nao a alunos cadastrados")
            return
        for professor in self.data:
            print(f"Matricula: {professor.matricula}, Nome: {professor.nome}, Carga Horária: {professor.cargaHoraria}, "
                  f"Idade: {professor.idade}, Salario {professor.salario}") 

    
    def editar(self, id):
        for professor in self.data:
            if professor.matricula == id:
                print("Professor encontrado!")
                
                nome = input("Digite o Nome do professor: ")
                idade = input("Digite a idade do professor: ")
                cargaHoraria = input("Digite a carga horaria do professor: ")
                salario = input("Digite o salario do professor: ")

                if nome:
                    professor.nome = nome
                if idade:
                    professor.idade = int(idade)
                if cargaHoraria:
                    professor.cargaHoraria = int(cargaHoraria)
                if salario:
                    professor.salario = float(salario)
                print("Alterações concluidas")
                return
        print("Professor não encontrado")
    
    def excluir(self,id: int):
        for professor in self.data:
            if professor.matricula == id:
                self.data.remove(professor)
                print(f"Professor de matricula numero {id} excluido!")
                return
        print("Aluno nao encontrado")