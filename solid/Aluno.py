from Disciplina import Disciplina

class Aluno:
    def __init__(self,id: int = 0, nome: str = '', idade: int = 0, curso: str = '' ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.discipliasCursadas = []
     
    def checarTipoId(self) -> int:
        try:
            id = int(input("Digite o ID do aluno: "))
            return id  
        except ValueError:
            print("Erro: O ID deve ser um número inteiro.")
            return self.checarTipoId()
        
    def checarTipoIdade(self) -> int:
        try:
            idade = int(input("Digite a idade do aluno: "))
            return idade  
        except ValueError:
            print("Erro: A idade deve ser um número inteiro.")
            return self.checarTipoIdade()

    def obterDados(self):
        id = self.checarTipoId()
        nome = input("Digite o Nome do Aluno: ")
        idade = self.checarTipoIdade()
        curso = input("Digite o curso do Aluno: ")
        return id,nome,idade,curso
            
    
    def criarAluno(self, alunos):
        id , nome, idade ,curso = self.obterDados()
        aluno = Aluno(id,nome,idade,curso)
        alunos.append(aluno)
        print("Aluno Adicionado!")
        
    def editarAluno(self,id: int, alunos):
        for aluno in alunos:
            
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