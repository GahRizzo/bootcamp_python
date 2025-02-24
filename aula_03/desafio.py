## Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, 
## imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

### Bugs possíveis:
## Usuário inserir um nome com números ou nome vazio
## Usuário utilizar valores negativos no salário
## Usuário digitar um texto no salário
## Usuário digitar um valor negativo no salário

### Inserindo loops no código

while True:
    try:
        name = input("Type your name: ")
        if name == "" or name.isspace():
            print('Empty input, please type your name')
        elif any(char.isdigit() for char in name):
            print('Type a string, not a number')
        else:
            break
    except ValueError as e:
        print(f'{e} - Type a number, not a empty or word/phrase')

while True:
    try:
        salary = float(input("Type your salary: "))

        if salary <= 0:
            print('Type a salary that greater than zero')
        else:
            break
    except ValueError as e:
        print(f'{e} - Type a number, not a empty or word/phrase')

while True:
    try:
        bonus_percentage = float(input("Type your bonus percentage: "))

        if bonus_percentage < 0:
            print('Type a non-negative percentage')
        else:
            break
    except ValueError as e:
        print(f'{e} - Type a number, not a empty or word/phrase')

bonus_value = 1000 + salary*(bonus_percentage/100)
print(f'💸💸💸   {name} your bonus in this year is .... ${bonus_value}   💸💸💸')