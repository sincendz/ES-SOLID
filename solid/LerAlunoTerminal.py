class LerAlunoTerminal:
    def tryCast(value, type):
        try:
            return type(value)
        except:
            return False

    def lerDoTerminal(self,type, prompt):
        input_value = input(prompt)
        while not self.tryCast(input_value, type):
            input_value = input(prompt)
        return self.tryCast(input_value, type)
    
    def obterDados(self):
        id = self.lerDoTerminal(int,"Digite o id do aluno: ")
        nome = self.lerDoTerminal(str,"Digite o nome do aluno: ")
        idade = self.lerDoTerminal(int,"Digite a idade do aluno: ")
        curso = self.lerDoTerminal(str,"Digite o curso do aluno")
        return id,nome,idade,curso
