from Aluno import Aluno
from LerAlunoTerminal import LerAlunoTerminal
from Crud import Crud


class AlunoServicos(Crud):
    def __init__(self):
        super().__init__()
        self.lerAlunoTerminal = LerAlunoTerminal()

    
    def criar(self):
        id , nome, idade ,curso = self.lerAlunoTerminal.obterDados()
        aluno = Aluno(id,nome,idade,curso)
        self.data.append(aluno)
        print("Aluno Adicionado!")
    
    def ver(self):
        if(len(self.data) == 0):
            print("Nao a alunos cadastrados")
            return
        for aluno in self.data:
            print(f"Id: {aluno.id}, Nome: {aluno.nome}, Idade : {aluno.idade}, Curso: {aluno.curso}")
    
    def editar(self, id):
        for aluno in self.data:
            
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
    
    def excluir(self,id: int):
        for aluno in self.data:
            print(aluno.id)
            if aluno.id == id:
                self.data.remove(aluno)
                print(f"Aluno de {id} excluido!")
                return
        print("Aluno nao encontrado")
        
            
class alunosIdadeMaiorQue20:
    def __init__(self, aluno_servicos: AlunoServicos):
        self.aluno_servicos = aluno_servicos

    def procurar(self):
        alunos = self.aluno_servicos.data  # Pega a lista de alunos diretamente de AlunoServicos
        for aluno in alunos:
            if aluno.idade > 20:
                print(aluno.nome)