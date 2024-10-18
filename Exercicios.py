print("hello world!")

valorA = float(input("Insira um valor: "))
valorB = float(input("Insira um valor: "))
soma = float(valorA) + float(valorB)
média = soma /2
print("Média: ", média)


#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade= input("Insira a idade: ");
nome= input("Insira o nome: ");
print(f"O meu nome é {nome} e tenho {idade} anos.");


#EX0.2
"""
EX0.2: Output
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá, Mundo!")
fruta= "maças"
print(f"Eu gosto de {fruta}.")


#EX0.3
"""
EX0.3: Input
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome= input("Digite o seu nome: ")
print(f"Bem-vindo {nome}.")
numero= int(input("Insira um numero inteiro: "))
dobro= numero * 2
print(f"O dobro de {numero} é {dobro}.")

#EX1.1
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
print("\nBem-vindos ao Python!")

#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
input("José, bem-vindo ao Python!\n")

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
valor= input("\nInsira um valor: ")
input(f"O valor é: {valor}")

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
print("Olá")
valor= input("Insira o seu primeiro e ultimo nome: ")
input(f"\nBom dia {valor}!")

#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome= input("Qual é o seu nome? ")
idade= input("Qual é a sua idade? ")
residência= input("Qual é a sua residência ? ")
print(f"O seu nome é{nome}:  ")
print(f"A sua idade é{idade}:  ")
print(f"A sua residência é{residência}:  ")

#1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguageProg = "Python"
nome = "Gonçalo Silva"

print(f"O {nome} sabe programar em {linguageProg}.")

#1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
print(f"{'Bem-vindo ao Python!' : <50}")
print(f"{'Bem-vindo ao Python!' : ^50}")
print(f"{'Bem-vindo ao Python!' : >50}")

#1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
raio = float(input("Insira o valor do raio: "))
area = 3,14 * (raio* 2) 
perimetro = 2 * 3,14 * raio
print(f"\nA area da circunferencia é {area} e o perimetro é {perimetro}.")

#1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
import datetime
x = datetime.datetime.now()
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%y")
hora = x.strftime("%H")
minutos = x.strftime("%M")
segundos = x.strftime("%S")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}/{dia}/{ano}")
print(f"{hora}:{minutos}:{segundos}")

#1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
numero= input("Insira o seu numero: ")
pontuacao= input("Insira a sua pontuação: ")
print(f"O atleta numero {numero} teve uma pontuação de {pontuacao}.")

#1.10
"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
dtnascimento = input("Insira a data do seu nascimento: ")
day,month,year = map(int, dtnascimento.split("-"))
today = datetime.date.today()
idade = today.year - year - ((today.month, today.day) < (month, day))
print("A tua idade é",idade,"anos.")

#1.11
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO).
"""
libras = float(input("Quantas libras quer inserir?: "))
euros = libras * 1.19
print(f"Dá um total de {euros} euros.")


#IF E ELSE
nota=int(input("Insira a sua nota: "))
if nota >=10:
  print("Aprovado")
  print("--FIM--")
else: 
  print("Reprovado")
  print("--FIM--")

#Ex FP1
numero = int(input("Introduza um número: "))
if numero == 0:
  print("O numero é igual a zero.")
elif numero <= 0:
  print("O numero é negativo.")
else:
  print("O numero é positivo")  

#Ex FP2
numero = int(input("Insira um numero: "))
if numero % 2 == 0:
  print("O numero é par.")
else:
  print("O numero é ímpar.")

#Ex FP3
"""
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"
"""
nota = int(input("Insira a nota final do aluno: "))
if nota < 10:
  print("Reprovado")
elif nota >= 10 and nota <= 14:
  print("Suficiente")
elif nota >= 15 and nota <= 17:
  print("Bom")
elif nota > 17:
  print("Muito Bom")

#Ex FP4
"""
Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.
"""
celsius = float(input("Insira a temperatura que pretende transformar: "))
Fahrenheit = celsius * 9/5 + 32
Kelvin = celsius + 273.15
print(f"Em graus farhrenheit fica {Fahrenheit} e em Kelvin fica {Kelvin}.")

#Ex FP5
"""
Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:
Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""
salario = float(input("Insira o valor do seu salário mensal: "))
if salario <= 1000:
  print("Isento de impostos")
elif salario >= 1001 and salario <= 2000:
  print("10% de imposto")
  imposto10 = salario * 0.1 
  print(f"Valor a pagar é {imposto10}.")
elif salario > 2000:
  print("20% de imposto")
  imposto11 = salario * 0.2
  print(f"Valor a pagar é {imposto11:.2f}.")


#FICHA PRÁTICA.002 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
"""
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""
for i in range(1,11):
  print(i)

"""
Exercício FP7: Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
"""
soma = 0
numero = 1
while numero <= 100:
    soma += numero
    numero += 1
print(f"A soma dos numeros de 1 a 100 é: {soma}")

"""
Exercício FP8: Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
"""
frase = input ("Insira uma frase: ")
vogais = 0
for letra in frase:
  if letra.lower() in "aeiou"
    vogais += 1
print(f"A frase tem {vogais} voigias.")

"""
Exercício FP9: Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
"""
for i in range (1, 51):
  if i % 5 == 0:
    print(i)

temporario = 0
for i in range (1,51):
  if temporario <= 49:
    temporario = i * 5
    print(temporario)

"""
Exercício FP10: Verificar se um número é primo.
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
[consola]
Introduza o número 1: 10
Introduza o número 2: 20
Introduza o número 3: 30
Introduza o número 4: 40
Introduza o número 5: 50
A média é: 30.0
"""
  notas = []
  for i in range(0,5):
    numeros = int(input(f"Introduza um numero {i+1}: "))
    notas.append(numeros) #adicionar um elemento à lista
  soma = sum(notas) #calcula a soma de todos os elementos dentro da lista
  x = len(notas) #devolve o número total de elementos dentro da lista
  media = (soma / x)
  print(f"A média é: {media}")

  """
  Exercício FP11: Média de uma lista de números.
  Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.

  [consola]
  Introduza um número: 13
  13 é um número primo.
  """
  numero = int(input("Insira um numero: "))
  divisores = 0
  for i in range(1, numero + 1):
      if numero % i == 0: #verifica se o resultado da divisao é 0
        divisores += 1 #incrementa o contador de divisores
  if divisores == 2:
      print(f"O {numero} é um numero primo.")
  else:
      print(f"O {numero} não é um numero primo")

"""
Exercício FP12: Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.

[consola]
Lista de números pares: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""
for i in range (1, 21):
  if i % 2 == 0:
    print(i)

"""
Exercício FP13: Inverter uma string.
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.

[consola]
Introduza uma palavra: Python
A palavra invertida é: nohtyP
"""
frase = str(input("Insira uma palavra: "))[::-1]
print(f"A palavra invertida é: {frase}")

"""
Exercício FP14: Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

[consola]
Introduza um número: 6
Tabuada de 6:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60
"""
num = int(input("Introduza um número: ")) 
for i in range(1,11):
  mult = num * i
  print(f"{num} x {i} = {mult}")

OU

num = int(input("Introduza um número: "))
i = 1
while i < 11:
  mult = num * i
  print(f"{num} x {i} = {mult}")
  i += 1

