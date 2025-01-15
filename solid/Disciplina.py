from Professor import Professor

class Disciplina():
    def __init__(self, codigo = '', nome: str = '', 
                 cargaHoraria: int = 0, professorResponsavel: Professor = None, creditos: int = 0):
        self.codigo = codigo
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.professorResponsavel = professorResponsavel
        self.creditos = creditos

    
    def criarDisciplina(self, disciplinas, professores):
        codigo = input("Digite o código da disciplina: ").upper()
        nome = input("Digite o nome da disciplina: ")
        cargaHoraria = int(input("Digite a carga horária da disciplina: "))
        creditos = int(input("Digite o número de créditos da disciplina: "))
        matriculaProfessor = int(input("Digite a matrícula do professor responsável: "))
        professorResponsavel = None
        for professor in professores:
            if professor.matricula == matriculaProfessor:
                professorResponsavel = professor
            
        if not professorResponsavel:
            print("Professor não encontrado. A disciplina não foi criada.")
            return

        disciplina = Disciplina(codigo, nome, cargaHoraria, professorResponsavel, creditos)
        disciplinas.append(disciplina)
        print("Disciplina adicionada!")
    def editarDisciplina(self,codigo,disciplinas,professores):
        for disciplina in disciplinas:
            if disciplina.codigo == codigo:
                print("Disciplina encontrado!")
                
                nome = input("Digite o Nome da disciplina: ")
                cargaHoraria = input("Digite a carga horaria da disciplina: ")
                matriculaProfessor = input("Digite a matricula do professor: ")
                creditos = input("Digite os creditos da disciplina: ")
                
                
                if nome:
                    disciplina.nome = nome
                if matriculaProfessor:
                    #Checar se o professor existe 
                    for professor in professores:
                        if professor.matricula == int(matriculaProfessor):
                            disciplina.professorResponsavel = professor
                            print(f"Professor:{professor.nome} Encontrado ")
                if cargaHoraria:
                    disciplina.cargaHoraria = int(cargaHoraria)
                if creditos:
                    disciplina.creditos = int(creditos)
                print("Alterações concluidas")
                return
        print("Disciplina não encontrada")

    def excluirDisciplina(self, codigo: int, disciplinas):
        for disciplina in disciplinas:
            if disciplina.codigo == codigo:
                disciplinas.remove(disciplina)
                print(f"Disciplina com código {codigo} foi deletada!")
                return
        print("Disciplina não encontrada.")
        
    def verDisciplinas(self,disciplinas):
        if len(disciplinas) == 0:
            print("Sem disciplinas cadastradas!")
            return
        for disciplina in disciplinas:
            print(f"Código: {disciplina.codigo}, Nome: {disciplina.nome}, Carga Horária: {disciplina.cargaHoraria}, "
                  f"Créditos: {disciplina.creditos}, Professor Responsável: {disciplina.professorResponsavel.nome}")