# ES-SOLID
 
# Aplicação de principios SOLID



## S — Responsabilidade Única (Single Responsibility Principle)

A responsabilidade única diz respeito ao nosso trecho de código (classe, função, etc.) realizar apenas uma coisa de forma bem feita. Ou seja, como o próprio nome diz, ter uma única responsabilidade. Ao fazer essa separação, o código fica mais legível, evita bugs e, caso ocorram, será bem mais fácil de controlá-los




### Exemplos sem SOLID

```python
class Aluno():
    def __init__(self,id: int = 0, nome: str = '', idade: int = 0, curso: str = '' ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.lerAlunoTerminal = LerAlunoTerminal()
            
    def criarAluno(self, alunos):
        #Logica
        
    def editarAluno(self,id: int, alunos):
        #Logica
    def excluirAluno(self,id: int, alunos):
        #Logica
    
    def verAlunos(self,alunos):
        #Logica
```
Nossa classe Aluno tem métodos de serviço do aluno que não são de sua responsabilidade. Então, a classe Aluno agora fica responsável apenas por instanciar o aluno, e a classe AlunoService faz as funções básicas do CRUD. Agora, cada função tem sua responsabilidade única.


### Exemplos com SOLID

```python
class Aluno():
    def __init__(self,id: int = 0, nome: str = '', idade: int = 0, curso: str = '' ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso
```
```python

class AlunoServicos:
    def __init__(self):
        self.lerAlunoTerminal = LerAlunoTerminal()

    def criarAluno(self, alunos):
        #Logica

    def editarAluno(self, id: int, alunos):
        #Logica

    def excluirAluno(self, id: int, alunos):
        #Logica
    
    def verAlunos(self, alunos):
        #Logica

```

## O — Aberto-Fechado ( Open/Closed Principle )

O princípio aberto/fechado diz o seguinte: 'As classes devem ser abertas para extensão, mas fechadas para modificação'. Ou seja, classes que já estão funcionando não devem ser modificadas. Caso seja necessário adicionar algo novo, deve-se realizar uma extensão.

### Técnicas para fazer isso:

#### 1. Herdar classes

#### 2. Uso de interfaces ou abstrações




```python
#Classe Aluno
rom Aluno import Aluno
from LerAlunoTerminal import LerAlunoTerminal

class AlunoServicos:
    def __init__(self):
        #Logica

    def criarAluno(self, alunos):
        #Logica
        
    def editarAluno(self, id: int, alunos):
        #Logica
        
    def excluirAluno(self, id: int, alunos):
        #Logica
    
    def verAlunos(self, alunos):
        #Logica
            
class AlunosIdadeMaiorQue20:
    def __init__(self, alunos):
        #Logica
        
    def procurar(self):
        #Logica
```

Perceba que foi necessário adicionar uma função na nossa classe, mas como ela está fechada para modificação e aberta para extensão, fizemos uma nova classe que faz o que o programador deseja. Isso é bem importante para que não ocorram erros ou para que o que já está funcionando não pare de funcionar.

