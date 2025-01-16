import os
import platform

from Aluno import Aluno
from Professor import Professor

alunos = []
professores = []
disciplinas = []

aluno = Aluno()
professor = Professor()


professorLucas = Professor(0,'Lucas',30,100,10_000)
professorVivi = Professor(1,'Viviane',35,200,20_000)




professores.append(professorLucas)
professores.append(professorVivi)



def limparTela():
    if platform.system() == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Linux/macOS


def menu():
    print("1 - Gerenciar Aluno")
    print("2 - Gerenciar Professor")
    print("5 - Sair")

def menuAluno():
    print("1 - Adicionar Aluno")
    print("2 - Editar Aluno")
    print("3 - Ver Alunos")
    print("4 - Excluir Aluno")
    print("5 - Voltar ao menu Principal")
    
def menuProfessor():
    print("1 - Adicionar Professor")
    print("2 - Editar Professor")
    print("3 - Ver Professors")
    print("4 - Excluir Professor")
    print("5 - Voltar ao menu Principal")
    

def escolhasAluno(escolhaAluno):
    if escolhaAluno == 1:
        limparTela()
        aluno.criarAluno(alunos)
        
    elif escolhaAluno == 2:
        limparTela()
        id = int(input("Digite o ID do aluno: "))
        aluno.editarAluno(id, alunos)
        
    elif escolhaAluno == 3:
        limparTela()
        aluno.verAlunos(alunos)
        
    elif escolhaAluno == 4:
        limparTela()
        id = int(input("Digite o ID do aluno: "))
        aluno.excluirAluno(id, alunos)
    
    elif escolhaAluno == 5:
        return False
    
    return True


def escolhasProfessor(escolhaProfessor):
    if escolhaProfessor == 1:
        limparTela()
        professor.criarProfessor(professores)
        
    elif escolhaProfessor == 2:
        limparTela()
        id = int(input("Digite o ID do professor: "))
        professor.editarProfessor(id, professores)
        
    elif escolhaProfessor == 3:
        limparTela()
        professor.verProfessores(professores)
        
    elif escolhaProfessor == 4:
        limparTela()
        matricula = int(input("Digite a matricula do professor: "))
        professor.excluirProfessor(matricula, professores)
    
    elif escolhaProfessor == 5:
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
    elif escolha == 5:
        limparTela()
        break
