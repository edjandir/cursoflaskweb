# 1-Introdução ao Python  
## História, Características e Aplicações

- Explorando a linguagem que transforma o mundo da programação.
- Criada para ser simples, poderosa e versátil.

---

## O que é Python?

- **Python** é uma linguagem de programação de alto nível criada em 1991.  
- Projetada para ser:
  - Simples e legível.
  - Versátil e poderosa.
- Usada em áreas como:
  - Ciência de dados.
  - Inteligência artificial.
  - Automação e desenvolvimento web.

---

## Origem do Python

- Criado por **Guido van Rossum** em dezembro de 1989 no CWI (Holanda).
- Inspirado na linguagem **ABC**, mas com funcionalidades aprimoradas.
- Nome inspirado no programa de comédia britânico:
  - *Monty Python's Flying Circus*.

---

## Primeira Versão

- Primeira versão (0.9.0) lançada em fevereiro de 1991.
- Incluía recursos como:
  - Classes com herança.
  - Tratamento de exceções.
  - Tipos nativos como listas e dicionários.
- Versão 1.0 lançada em janeiro de 1994.

---

## Filosofia do Python

> "There should be one—and preferably only one—obvious way to do it."  
> *(PEP 20)*

- Código deve ser legível e simples.  
- Uso de indentação em vez de chaves `{}` para delimitar blocos de código.

Exemplo:
```python
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
---

## Características Principais

1. **Sintaxe Simples**: Fácil de aprender e entender.  
2. **Interpretada**: Executa o código linha por linha.  
3. **Tipagem Dinâmica**: Não exige declaração explícita de tipos.  
4. **Multiparadigma**: Suporta programação orientada a objetos, funcional e procedural.

---

## Biblioteca Padrão Ampla

- Biblioteca padrão rica com módulos para:
  - Manipulação de arquivos.
  - Acesso a bancos de dados.
  - Processamento de texto.
- Ecossistema robusto com bibliotecas externas, como:
  - **NumPy**, **Pandas**, **Django**, entre outros.

---

## Principais Aplicações

1. **Ciência de Dados e IA**  
   - Bibliotecas: TensorFlow, Pandas, Matplotlib.
2. **Desenvolvimento Web**  
   - Frameworks: Django, Flask.
3. **Automação**  
   - Scripts para tarefas repetitivas.
4. **IoT (Internet das Coisas)**  
   - Controle de dispositivos com Raspberry Pi.
---


# 2-Variáveis e Tipos de Dados em Python  
## Conceitos Fundamentais

- Variáveis são usadas para armazenar valores na memória.
- Tipos de dados definem a natureza dos valores armazenados.
- Python é uma linguagem de **tipagem dinâmica**, ou seja, não é necessário declarar o tipo da variável explicitamente.

---

## Criando Variáveis

- Em Python, basta atribuir um valor a um nome para criar uma variável:
```python
x = 10
nome = "Maria"
altura = 1.75
print(x, nome, altura)
```
- Regras para nomes de variáveis:
  - Devem começar com uma letra ou underscore (_).
  - Não podem conter espaços ou caracteres especiais.
  - São sensíveis a maiúsculas e minúsculas (exemplo: idade ≠ Idade).

---

## Tipos de Dados Básicos

- **int**: Números inteiros.
- **float**: Números decimais.
- **str**: Sequências de caracteres (strings).
- **bool**: Valores lógicos (True ou False).

Exemplo:
```python
idade = 25       # int
altura = 1.75    # float
nome = "João"    # str
ativo = True     # bool

print(type(idade), type(altura), type(nome), type(ativo))
```
---

## Conversão de Tipos

- Use funções como int(), float(), str() e bool() para converter tipos de dados:
```python
idade = "25"
idade_inteira = int(idade)
print(idade_inteira)  # Converte string para inteiro

altura = 1.75
altura_texto = str(altura)
print(altura_texto)   # Converte float para string

ativo = "True"
ativo_bool = bool(ativo)
print(ativo_bool)     # Converte string para booleano
```
---

## Exercício Prático

Peça ao usuário seu nome, idade e altura. Exiba os valores e seus respectivos tipos:
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
```
---
# 3-Entrada de Dados e Exibição de Dados

- A função `input()` permite que o usuário insira dados no programa.
- Sempre retorna uma **string**:
```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```
---

## Convertendo Tipos de Entrada

- Use funções como `int()`, `float()` ou `bool()` para converter a entrada:
```python
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
ativo = bool(int(input("Está ativo? (1 para Sim, 0 para Não): ")))
```
---

## Exibição de Dados com `print()`

- A função `print()` exibe informações no console.
- Aceita múltiplos argumentos:
```python
print("Nome:", nome, "Idade:", idade)
```
- Formatação com **f-strings**:
```python
print(f"{nome} tem {idade} anos e mede {altura:.2f} metros.")
```
---

## Exercício Prático

Crie um programa que peça ao usuário seu nome, idade e cidade, e exiba uma mensagem formatada:
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")

print(f"{nome}, {idade} anos, mora em {cidade}.")
```
---

# 4-Estruturas de Decisão

- Permitem executar diferentes blocos de código com base em condições.
- Exemplo básico:
```python
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
---

## Condicional `if`, `elif` e `else`

- Estrutura completa:
```python
if condicao1:
    # Código se condicao1 for verdadeira
elif condicao2:
    # Código se condicao2 for verdadeira
else:
    # Código se nenhuma condição for verdadeira
```
---

## Condições Aninhadas
```python
nota = float(input("Digite sua nota: "))

if nota >= 7:
    if nota == 10:
        print("Parabéns! Nota máxima!")
    else:
        print("Aprovado!")
else:
    print("Reprovado.")
```
---

## Exercício Prático

Peça ao usuário sua idade e diga se ele pode votar ou dirigir:
```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode votar e dirigir.")
elif idade >= 16:
    print("Você pode votar, mas não pode dirigir.")
else:
    print("Você não pode votar nem dirigir.")
```
---

# Estruturas de Repetição

- Estruturas que repetem um bloco de código enquanto uma condição é verdadeira.
- Tipos principais em Python:
   - **for loop**
   - **while loop**

---

## Loop `for`

- Itera sobre sequências (listas, strings, etc.):
```python
for i in range(5):
    print(i) # Saída: 0, 1, 2, 3, 4
```
---

## Loop `while`

- Repete enquanto a condição for verdadeira:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
---

## Controle de Loops (`break` e `continue`)
```python
for i in range(10):
    if i == 5:
        break # Encerra o loop
    if i % 2 == 0:
        continue # Pula para a próxima iteração
    print(i)
```
---

## Exercício Prático

Crie um programa que peça números ao usuário até ele digitar "sair":
```python
while True:
    entrada = input("Digite um número ou 'sair': ")
    if entrada == "sair":
        break
    print(f"Você digitou {entrada}")
```
---

# 5-Funções

- Blocos reutilizáveis de código que executam uma tarefa específica.
- Definidas com a palavra-chave `def`.

Exemplo básico:
```python
def saudacao(nome):
    return f"Olá, {nome}!"
    
print(saudacao("Maria"))
```
---

## Parâmetros e Valores Padrão
```python
def soma(a, b=0):
    return a + b

print(soma(10))      # Usa valor padrão b=0 -> Saída: 10
print(soma(10, 5))   # Saída: 15
```
---

## Funções Recursivas

Funções podem chamar a si mesmas (recursão):
```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(5)) # Saída: 120
```
---

## Exercício Prático

Crie uma função que receba dois números e retorne o maior deles.
```python
def maior_numero(a, b):
    if a > b:
        return a
    return b

print(maior_numero(10, 20))
```

# 6-Manipulação de *Strings* em Python  
## Operações e Exemplos Práticos

- Strings são sequências de caracteres.
- Python oferece métodos e operadores poderosos para manipulá-las.

---

## Criando Strings

- Strings podem ser criadas usando aspas simples ou duplas:
```python
texto1 = 'Olá, Mundo!'
texto2 = "Python é incrível!"
print(texto1)
print(texto2)
```
- Strings também podem conter aspas dentro delas:
```python
texto = "Ele disse: 'Python é ótimo!'"
print(texto)
```
---

## Acessando Caracteres em Strings

- Use índices para acessar caracteres individuais:
```python
texto = "Python"
print(texto[0])  # Primeiro caractere: P
print(texto[-1]) # Último caractere: n
```
- Use slicing para acessar partes da string:
```python
print(texto[0:3])  # Pyt (do índice 0 ao 2)
print(texto[::2])  # Pto (passos de 2)
```
---

## Concatenando e Repetindo Strings

- Concatene strings com o operador +:
```python
saudacao = "Olá"
nome = "Maria"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)
```
- Repita strings com o operador *:
```python
repeticao = "Python! " * 3
print(repeticao)  # Python! Python! Python!
```
---

## Métodos de Alteração de *Case*

- Converta para maiúsculas ou minúsculas:
```python
texto = "Python é incrível!"
print(texto.upper())   # PYTHON É INCRÍVEL!
print(texto.lower())   # python é incrível!
```
```python
- Capitalize a primeira letra:
print(texto.capitalize())  # Python é incrível!
```
---

## Removendo Espaços e Caracteres

- Use strip() para remover espaços extras:
```python
texto = "   Olá, Mundo!   "
print(texto.strip())    # Remove espaços nas extremidades
```
- Remova caracteres específicos:
```python
texto = "***Python***"
print(texto.strip("*"))  # Remove os asteriscos (*)
```
---

## Dividindo e Unindo Strings

- Divida uma string em uma lista com split():
```python
texto = "Maçã, Banana, Laranja"
frutas = texto.split(", ")
print(frutas)  # ['Maçã', 'Banana', 'Laranja']

- Una elementos de uma lista em uma string com join():
frutas_unidas = ", ".join(frutas)
print(frutas_unidas)  # Maçã, Banana, Laranja
```
---

## Substituindo Substrings

- Substitua partes de uma string com replace():
```python
texto = "Eu gosto de Java."
novo_texto = texto.replace("Java", "Python")
print(novo_texto)  # Eu gosto de Python.
```
---

## Verificando o Conteúdo da String

- Verifique se a string começa ou termina com algo específico:
```python
texto = "Aprendendo Python"
print(texto.startswith("Aprendendo"))  # True
print(texto.endswith("Java"))          # False
```
- Verifique se a string contém apenas números ou letras:
```python
codigo = "12345"
print(codigo.isdigit())  # True (só contém números)
nome = "Maria"
print(nome.isalpha())    # True (só contém letras)
```
---

## Exercício Prático

Peça ao usuário um texto e manipule-o:

1. Converta o texto para maiúsculas.
2. Divida o texto em palavras.
3. Substitua uma palavra específica.
```python
texto = input("Digite um texto: ")
print("Maiúsculas:", texto.upper())
palavras = texto.split()
print("Palavras:", palavras)
novo_texto = texto.replace("Python", "programação")
print("Texto modificado:", novo_texto)
```
---

# 7-Listas em Python  
## Estruturas de Dados Fundamentais

- Listas são coleções ordenadas e mutáveis que permitem armazenar múltiplos valores.
- São definidas usando colchetes `[]` e podem conter diferentes tipos de dados.

Exemplo:
```python
frutas = ["maçã", "banana", "laranja"]
print(frutas)
```
---

# Criando e Acessando Elementos

- Criação de listas:
```python
numeros = [1, 2, 3, 4, 5]
misturados = [1, "Python", True, 3.14]
```
- Acessando elementos por índice:
```python
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # maçã
print(frutas[-1]) # laranja (último elemento)
```
- Alterando elementos:
```python
frutas[1] = "uva"
print(frutas)  # ["maçã", "uva", "laranja"]
```
---

# Métodos Comuns de Listas

- Adicionar elementos:
```python
frutas.append("abacaxi")  # Adiciona ao final
frutas.insert(1, "morango")  # Insere no índice especificado
```
- Remover elementos:
```python
frutas.remove("banana")  # Remove o primeiro elemento encontrado
ultimo = frutas.pop()    # Remove e retorna o último elemento
print(ultimo)
```
- Contar ocorrências:
```python
numeros = [1, 2, 2, 3]
print(numeros.count(2))  # Saída: 2
```
---

# Iterando Sobre Listas

- Use loops para percorrer os elementos de uma lista:
```python
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)
```
- Use `enumerate()` para obter o índice e o valor:
```python
for indice, valor in enumerate(numeros):
    print(f"Índice {indice}: {valor}")
```
---

# Operações com Listas

- Concatenação:
```python
lista1 = [1, 2]
lista2 = [3, 4]
resultado = lista1 + lista2
print(resultado)  # [1, 2, 3, 4]
```
- Repetição:
```python
repetida = ["Python"] * 3
print(repetida)  # ["Python", "Python", "Python"]
```
- Verificar existência:

```python
print(3 in numeros)   # True
print(5 not in numeros)   # False
```
---

## Ordenação e Inversão

- Ordenar uma lista:
```python
numeros = [4, 2, 8, 5]
numeros.sort()       # Ordena a lista em ordem crescente
numeros.sort(reverse=True)   # Ordena em ordem decrescente
```
- Inverter a ordem dos elementos:
```python
numeros.reverse()
print(numeros)
```
---

## List Comprehension

- Crie listas de forma concisa usando list comprehension:
```python
quadrados = [x**2 for x in range(5)]
print(quadrados)   # [0, 1, 4, 9, 16]
```
- Filtrar elementos com condições:
```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)   # [0, 2, 4, 6, 8]
```
---

## Exercício Prático com Listas

Crie uma lista com números fornecidos pelo usuário. Calcule a soma dos números e exiba os valores pares:

```python
numeros = []
for i in range(5):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

soma = sum(numeros)
pares = [x for x in numeros if x % 2 == 0]

print(f"Números digitados: {numeros}")
print(f"Soma dos números: {soma}")
print(f"Números pares: {pares}")
```
---


# 8-Manipulação de Arquivos em Python  
### Conceitos Fundamentais

- Python oferece suporte nativo para manipular arquivos.
- Use a função `open()` para abrir arquivos.
- Modos de abertura comuns:
  - `"r"`: Leitura.
  - `"w"`: Escrita (sobrescreve o arquivo).
  - `"a"`: Adicionar conteúdo ao final.
  - `"r+"`: Leitura e escrita.

Exemplo:
```python
arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
```
---

## Lendo Arquivos

- Abra o arquivo no modo `"r"` para leitura:
```python
arquivo = open("exemplo.txt", "r")
```
- Métodos comuns:
  - `read()`: Lê todo o conteúdo do arquivo.
  - `readline()`: Lê uma linha por vez.
  - `readlines()`: Retorna uma lista com todas as linhas.

Exemplo:
```python
arquivo = open("exemplo.txt", "r")
for linha in arquivo:
    print(linha.strip())
arquivo.close()
```
---

## Escrevendo em Arquivos

- Abra o arquivo no modo `"w"` para sobrescrever ou `"a"` para adicionar conteúdo:
```python
arquivo = open("exemplo.txt", "w")
arquivo.write("Este é um exemplo de escrita.\n")
arquivo.write("Python facilita a manipulação de arquivos.\n")
arquivo.close()
```
- Atenção: O modo `"w"` apaga todo o conteúdo existente no arquivo.

---

## Usando `with open()`

- A abordagem `with open()` é recomendada porque fecha o arquivo automaticamente após o uso:
```python
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```
- Para escrever:
```python
with open("exemplo.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada.\n")
```
---

## Exercício Prático com Arquivos

1. Crie um programa que leia um arquivo linha por linha e exiba no console.
2. Se o arquivo não existir, crie-o e adicione algumas linhas.
```python
try:
    with open("meu_arquivo.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())
except FileNotFoundError:
    with open("meu_arquivo.txt", "w") as arquivo:
        arquivo.write("Linha 1\n")
        arquivo.write("Linha 2\n")
        print("Arquivo criado com sucesso!")
```
---
# 9-Programação Orientada por Objetos (POO) em Python  
## Introdução

- A Programação Orientada por Objetos (POO) é um paradigma que organiza o código em objetos.
- Python suporta POO com conceitos como classes, objetos, herança e polimorfismo.
- Benefícios:
  - Reutilização de código.
  - Modularidade.
  - Facilidade de manutenção.

---

## Classes e Objetos

- Uma **classe** é um modelo para criar objetos.
- Um **objeto** é uma instância de uma classe.

Exemplo:
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa("João", 25)
print(pessoa1.nome)  # João
print(pessoa1.idade) # 25
```
---

## Atributos e Métodos

- **Atributos** são variáveis associadas a uma classe ou objeto.
- **Métodos** são funções definidas dentro de uma classe.

Exemplo:
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Maria", 30)
pessoa1.apresentar()
```
---

## Atributos de Classe vs. Atributos de Instância

- **Atributos de instância** pertencem a cada objeto individualmente.
- **Atributos de classe** são compartilhados por todas as instâncias da classe.

Exemplo:
```python
class Pessoa:
    especie = "Humano"  # Atributo de classe

    def __init__(self, nome):
        self.nome = nome  # Atributo de instância

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

print(pessoa1.especie)  # Humano
print(pessoa2.especie)  # Humano
```
---

## Encapsulamento

- O encapsulamento protege os dados de acesso direto.
- Use underscores para indicar atributos privados.

Exemplo:
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def exibir_saldo(self):
        print(f"Saldo: {self.__saldo}")

conta = ContaBancaria(1000)
conta.depositar(500)
conta.exibir_saldo()
```
---

## Herança

- Herança permite que uma classe reutilize atributos e métodos de outra classe.

Exemplo:
```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print("Som genérico")

class Cachorro(Animal):
    def falar(self):
        print("Au au!")

cachorro = Cachorro("Rex")
cachorro.falar()  # Au au!
```
---

## Polimorfismo

- Polimorfismo permite que métodos com o mesmo nome tenham comportamentos diferentes dependendo da classe.

Exemplo:
```python 
class Forma:
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

quadrado = Quadrado(4)
print(quadrado.area())  # 16
```
---

## Métodos Especiais (Dunder Methods)

- Métodos especiais começam e terminam com dois underscores (`__`).
- Exemplo: `__init__`, `__str__`, `__repr__`.

Exemplo:
```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

pessoa = Pessoa("Ana", 22)
print(pessoa)
```
---

# Classes Abstratas

- Classes abstratas servem como base para outras classes e não podem ser instanciadas diretamente.
- Use o módulo `abc` para criar classes abstratas.

Exemplo:
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

circulo = Circulo(5)
print(circulo.area())
```
---

# Exercício Prático com POO

Crie uma classe `Carro` com os seguintes atributos e métodos:

1. Atributos: marca, modelo e ano.
2. Métodos: exibir informações do carro e calcular a idade do carro.
```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir_informacoes(self):
        print(f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}")
    
    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano

carro1 = Carro("Toyota", "Corolla", 2015)
carro1.exibir_informacoes()
print(f"Idade do carro: {carro1.calcular_idade(2023)} anos")