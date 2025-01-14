from Disciplina import Disciplina

class Aluno:
    def __init__(self,id: int = 0, nome: str = '', idade: int = 0, curso: str = '' ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.discipliasCursadas = []
        
    def criarAluno(self, alunos):
        id = int(input("Digite o ID do aluno: "))
        nome = input("Digite o Nome do Aluno: ")
        idade = input("Digite a idade do Aluno: ")
        curso = input("Digite o curso do Aluno: ")
        aluno = Aluno(id,str(nome),int(idade),str(curso))
        alunos.append(aluno)
        print("Aluno Adicionado!")
        
    def editarAluno(self,id: int, alunos):
        for aluno in alunos:
            print(aluno.id)
            if aluno.id == id:
                print("Aluno encontrado")
                nome = input("Digite o Nome do Aluno: ")
                idade = input("Digite a idade do Aluno: ")
                curso = input("Digite o curso do Aluno: ")
                if nome != '':
                    aluno.nome = nome
                if idade:
                    aluno.idade = int(idade)
                if curso != '':
                    aluno.curso = curso
                return
        print("Aluno nao encontrado")
        
    def excluirAluno(self,id: int, alunos):
        for aluno in alunos:
            print(aluno.id)
            if aluno.id == id:
                alunos.remove(aluno)
                print(f"Aluno de {id} excluido!")
                return
        print("Aluno nao encontrado")
    
    def verAlunos(self,alunos):
        if(len(alunos) == 0):
            print("Nao a alunos cadastrados")
            return
        for aluno in alunos:
            print(f"Id: {aluno.id}, Nome: {aluno.nome}, Idade : {aluno.idade}, Curso: {aluno.curso}")