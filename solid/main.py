import os
import platform

from AlunoServicos import AlunoServicos , alunosIdadeMaiorQue20
from Professor import Professor
from Disciplina import Disciplina
from Aluno import Aluno


alunos = []
professores = []
disciplinas = []

aluno = AlunoServicos()
professor = Professor()
disciplina = Disciplina()

alunoMario = Aluno(10,"Mario",20,"CC")
alunoG = Aluno(11,"Gustavo",21,"CC")
alunoJ = Aluno(12,"JOJE",22,"CC")
alunoGI = Aluno(12,"GUIGUI",19,"CC")

professorLucas = Professor(0,'Lucas',30,100,10_000)
professorVivi = Professor(1,'Viviane',35,200,20_000)

ES = Disciplina('QXD001',"ES",100,professorLucas,6)
PAA = Disciplina('QXD002','PAA',100,professorVivi,6)


alunos.append(alunoMario)
alunos.append(alunoG)
alunos.append(alunoJ)
alunos.append(alunoGI)

professores.append(professorLucas)
professores.append(professorVivi)

disciplinas.append(ES)
disciplinas.append(PAA)


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
        
    elif escolhaAluno == 6:
        aluIdade = alunosIdadeMaiorQue20(alunos)
        aluIdade.procurar()
    
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
