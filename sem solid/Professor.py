from Disciplina import Disciplina

class Professor:
    def __init__(self,matricula: int = 0 ,  nome: str = '', idade: int = 0, cargaHoraria: int = 0, salario: float = 0 ):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.cargaHoraria = cargaHoraria
        self.salario = salario
        self.discipliasMinistradas = []
        
    def criarProfessor(self,professores):
        matricula = int(input("Digite a matricula do professor: "))
        nome = input("Digite o Nome do professor: ")
        idade = int(input("Digite a idade do professor: "))
        cargaHoraria = int(input("Digite a carga horaria do professor: "))
        salario = float(input("Digite o salario do professor: "))
        professor = Professor(matricula,nome,idade,cargaHoraria,salario)
        professores.append(professor)
        print("Professor Adicionado!")
        
    def editarProfessor(self,matricula,professores):
        for professor in professores:
            if professor.matricula == matricula:
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
            
    def excluirProfessor(self,matricula, professores):
        for professor in professores:
            if professor.matricula == matricula:
                professores.remove(professor)
                print(f"Professor com matricula {matricula} foi deletado!")
                return
        print("Professor não encontrado")

    def verProfessores(self,professores):
        if len(professores) == 0:
            print("Lista de professores vazia!")
            return
        for professor in professores:
            print(f"Matricula: {professor.matricula}, Nome: {professor.nome}, Idade: {professor.idade}, Carga Horária: {professor.cargaHoraria}, Salário: {professor.salario}")
