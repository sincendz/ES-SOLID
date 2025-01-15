# ES-SOLID
 
# Aplicação de principios SOLID



## S — Responsabilidade Única

A responsabilidade única diz respeito ao nosso trecho de código (classe, função, etc.) realizar apenas uma coisa de forma bem feita. Ou seja, como o próprio nome diz, ter uma única responsabilidade. Ao fazer essa separação, o código fica mais legível, evita bugs e, caso ocorram, será bem mais fácil de controlá-los




### Exemplos sem SOLID

```python
def criarAluno(self, alunos):
        try:
            id = int(input("Digite o ID do aluno: "))
        except ValueError:
            print("Erro: O id deve ser um número inteiro.")
            return
            
        nome = input("Digite o Nome do Aluno: ")
        try:
            
            idade = input("Digite a idade do Aluno: ")
        except ValueError:
            print("Erro: A idade deve ser um número inteiro.")
            return
        
        curso = input("Digite o curso do Aluno: ")
        aluno = Aluno(id,str(nome),int(idade),str(curso))
        alunos.append(aluno)
        print("Aluno Adicionado!")
```
Por mais que o código seja simples, a presença desse tratamento de exceção pode prejudicar a legibilidade do código e dificultar sua manutenção


### Exemplos com SOLID

```python
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

        
    def criarAluno(self, alunos):
        id = self.checarTipoId()
        nome = input("Digite o Nome do Aluno: ")
        idade = self.checarTipoIdade()
        curso = input("Digite o curso do Aluno: ")
        aluno = Aluno(id,str(nome),int(idade),str(curso))
        alunos.append(aluno)
        print("Aluno Adicionado!")
```
Perceba que a diferença não foi tanta, mas vamos pensar em um código com várias e várias verificações. Essa prática de cada parte do código ter apenas uma responsabilidade ajuda bastante.

