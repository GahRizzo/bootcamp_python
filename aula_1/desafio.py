## Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, 
## imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

name = input("Type your name: ")
salary = float(input("Type your salary: "))
bonus_percentage = float(input("Type your bonus percentage: "))/100

bonus_value = 1000 + salary*bonus_percentage

print(f'{name} your bonus in this year is .... ${bonus_value}')

### Bugs possíveis:
## Usuário inserir um nome com números
## Usuário utilizar valores negativos no salário
## Usuário digitar um texto no salário
## Usuário digitar sem o formato de percentual
## Usuário digitar um valor negativo no salário