# ES-SOLID
 
# Aplicação de principios SOLID



## S — Responsabilidade Única (Single Responsibility Principle)

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

Por mais que tenhamos feito uma boa mudança, nossa classe CriarAluno ainda faz mais coisas do que deveria. Repare que ela também está obtendo os parâmetros. Então nossa função deveria se chamar CriarAlunoEObterValores()?

### Exemplos com SOLID Melhorado


```python
def obter_dados(self):
        id = self.checarTipoId()
        nome = input("Digite o Nome do Aluno: ")
        idade = self.checarTipoIdade()
        curso = input("Digite o curso do Aluno: ")
        return id,nome,idade,curso
            
    
    def criarAluno(self, alunos):
        id , nome, idade ,curso = self.obter_dados()
        aluno = Aluno(id,nome,idade,curso)
        alunos.append(aluno)
        print("Aluno Adicionado!")
```

Agora sim, nossa função faz exatamente o que seu nome diz: cria um aluno. Mas pera aí, ela também salva no array. Então a função deveria ter o nome CriarAlunoESalvarNoArray()? Aiai, larga de problema, rapaz...




## O — Aberto-Fechado ( Open/Closed Principle )

O princípio aberto/fechado diz o seguinte: 'As classes devem ser abertas para extensão, mas fechadas para modificação'. Ou seja, classes que já estão funcionando não devem ser modificadas. Caso seja necessário adicionar algo novo, deve-se realizar uma extensão.

### Técnicas para fazer isso:

#### 1. Herdar classes

#### 2. Uso de interfaces ou abstrações





### Exemplos sem SOLID

```python
#Classe Aluno
def verAlunos(self,alunos):
        if(len(alunos) == 0):
            print("Nao a alunos cadastrados")
            return
        for aluno in alunos:
            print(f"Id: {aluno.id}, Nome: {aluno.nome}, Idade : {aluno.idade}, Curso: {aluno.curso}")
```


```python
#Classe Disciplina
def verDisciplinas(self,disciplinas):
        if len(disciplinas) == 0:
            print("Sem disciplinas cadastradas!")
            return
        for disciplina in disciplinas:
            print(f"Código: {disciplina.codigo}, Nome: {disciplina.nome}, Carga Horária: {disciplina.cargaHoraria}, "
                  f"Créditos: {disciplina.creditos}, Professor Responsável: {disciplina.professorResponsavel.nome}")
```


```python
#Classe Professor
def verProfessores(self,professores):
        if len(professores) == 0:
            print("Lista de professores vazia!")
            return
        for professor in professores:
            print(f"Matricula: {professor.matricula}, Nome: {professor.nome}, Idade: {professor.idade}, Carga Horária: {professor.cargaHoraria}, Salário: {professor.salario}")
```
Podemos ver que todas as funções implementam a mesma coisa. Então, caso eu crie uma nova classe Diretor, precisarei criar o verDiretor. Será que existe alguma forma de mostrar todas essas entidades usando uma função genérica?


### Exemplos com SOLID


```python
from abc import ABC, abstractmethod

class Entidade(ABC):
    @abstractmethod
    #Qualquer classe que herda de entidade implementa o __str__
    #__str__ serve para printar printar o objeto
    def __str__(self):
        pass
```
Aberto para extensão: Agora conseguimos adicionar novas funcionalidades ao sistema sem alterar o código.

Fechado para modificação: O código existente já foi testado e está funcionando, então não devemos modificá-lo para adicionar novas funcionalidades
```python
class Aluno(Entidade):
    def __init__(self,id: int = 0, nome: str = '', idade: int = 0, curso: str = '' ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.lerAlunoTerminal = LerAlunoTerminal()
            
    def __str__(self):
        return f"Id: {self.id}, Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"
```

```python
def __init__(self,matricula: int = 0 ,  nome: str = '', idade: int = 0, cargaHoraria: int = 0, salario: float = 0 ):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.cargaHoraria = cargaHoraria
        self.salario = salario
        self.discipliasMinistradas = []
        
    def __str__(self):
        return f"Matricula: {self.matricula}, Nome: {self.nome}, Idade: {self.idade},
    Carga Horária: {self.cargaHoraria}, Salário: {self.salario}"
```

```python
class Disciplina(Entidade):
    def __init__(self, codigo = '', nome: str = '', 
                 cargaHoraria: int = 0, professorResponsavel: Professor = None, creditos: int = 0):
        self.codigo = codigo
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.professorResponsavel = professorResponsavel
        self.creditos = creditos

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Carga Horária: {self.cargaHoraria},
    Créditos: {self.creditos}, Professor Responsável: {self.professorResponsavel.nome}"
```
Com isso, agora podemos criar uma única função genérica que qualquer tipo de entidade que herde o método exibir poderá usar.


```python
class Visualizador:
    def verEntidades(self, entidades):
        if not entidades:
            print("Nenhuma entidade cadastrada.")
            return

        for entidade in entidades:
            print(entidade)
```

Agora, qualquer classe pode chamar visualizador.verEntidades(param) e os valores irão aparecer.