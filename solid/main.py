import os
import platform

from AlunoServicos import AlunoServicos , alunosIdadeMaiorQue20
from ProfessorServicos import ProfessorServicos
from Professor import Professor
from Disciplina import Disciplina
from Aluno import Aluno



professores = []
disciplinas = []

alunoServicos = AlunoServicos()
professorServisos = ProfessorServicos()
professor = Professor()
disciplina = Disciplina()



def limparTela():
    if platform.system() == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Linux/macOS


def menu():
    print("1 - Gerenciar Aluno")
    print("2 - Gerenciar Professor")
    print("3 - Gerenciar Disciplinas")
    print("5 - Sair")

def menuAluno():
    print("1 - Adicionar Aluno")
    print("2 - Editar Aluno")
    print("3 - Ver Alunos")
    print("4 - Excluir Aluno")
    print("5 - Voltar ao menu Principal")
    print("6 - Alunos com idade maior que 20")
    
def menuProfessor():
    print("1 - Adicionar Professor")
    print("2 - Editar Professor")
    print("3 - Ver Professors")
    print("4 - Excluir Professor")
    print("5 - Voltar ao menu Principal")
    
def menuDisciplina():
    print("1 - Adicionar Disciplina")
    print("2 - Editar Disciplina")
    print("3 - Ver Disciplinas")
    print("4 - Excluir Disciplina")
    print("5 - Voltar ao menu Principal")
    
def escolhasAluno(escolhaAluno):
    if escolhaAluno == 1:
        limparTela()
        alunoServicos.criar()
        
    elif escolhaAluno == 2:
        limparTela()
        id = int(input("Digite o ID do aluno: "))
        alunoServicos.editar(id)
        
    elif escolhaAluno == 3:
        limparTela()
        alunoServicos.ver()
        
    elif escolhaAluno == 4:
        limparTela()
        id = int(input("Digite o ID do aluno: "))
        alunoServicos.excluir(id)
        
    elif escolhaAluno == 6:
        #alunos = alunoServicos.atualizacaoData()
        aluIdade = alunosIdadeMaiorQue20(alunoServicos)
        aluIdade.procurar()
    
    elif escolhaAluno == 5:
        return False
    
    return True


def escolhasProfessor(escolhaProfessor):
    if escolhaProfessor == 1:
        limparTela()
        professorServisos.criar()
        
    elif escolhaProfessor == 2:
        limparTela()
        id = int(input("Digite a matricula do professor: "))
        professorServisos.editar(id)
        
    elif escolhaProfessor == 3:
        limparTela()
        professorServisos.ver()
        
    elif escolhaProfessor == 4:
        limparTela()
        matricula = int(input("Digite a matricula do professor: "))
        professorServisos.excluir(matricula)
    
    elif escolhaProfessor == 5:
        return False
    
    return True

    
def escolhasDisciplina(escolhaDisciplina):
    if escolhaDisciplina == 1:
        limparTela()
        disciplina.criarDisciplina(disciplinas,professores)
    
    elif escolhaDisciplina == 2:
        limparTela()
        codigo = input("Codigo disciplina(QXD---): ")
        print(codigo)
        disciplina.editarDisciplina(codigo,disciplinas,professores)
        
    elif escolhaDisciplina == 3:
        limparTela()
        disciplina.verDisciplinas(disciplinas)
        
        
    elif escolhaDisciplina == 4:
        limparTela()
        codigo = input("Codigo disciplina(QXD---): ")
        disciplina.excluirDisciplina(codigo,disciplinas)
        
    
    elif escolhaDisciplina == 5:
        return False
    
    return True
    



while(True):
    menu()
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        while(True):
            menuAluno()
            escolhaAluno = int(input("Digite sua escolha: "))
            if not escolhasAluno(escolhaAluno):
                limparTela()
                break
    if escolha == 2:
        while(True):
            menuProfessor()
            escolhaProfessor = int(input("Digite sua escolha: "))
            if not escolhasProfessor(escolhaProfessor):
                limparTela()
                break
    if escolha == 3:
        while(True):
            menuDisciplina()
            escolhaDisciplina = int(input("Digite sua escolha: "))
            if not escolhasDisciplina(escolhaDisciplina):
                limparTela()
                break
    elif escolha == 5:
        limparTela()
        break
