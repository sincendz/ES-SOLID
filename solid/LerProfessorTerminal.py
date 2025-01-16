class LerProfessorTerminal:
    def tryCast(self, value, type):
        try:
            return type(value)
        except:
            return False

    def lerDoTerminal(self, type, prompt):
        input_value = input(prompt)
        while not self.tryCast(input_value, type):
            input_value = input(prompt)
        return self.tryCast(input_value, type)
    
    def obterDados(self):
        matricula = self.lerDoTerminal(int,"Digite o matricula do professor: ")
        nome = self.lerDoTerminal(str,"Digite o nome do professor: ")
        idade = self.lerDoTerminal(int,"Digite a idade do professor: ")
        cargaHoraria = self.lerDoTerminal(int,"Digite a carga horaria do professor: ")
        salario = self.lerDoTerminal(int,"Digite a carga horaria do professor: ")

        return matricula,nome,idade,cargaHoraria, salario
