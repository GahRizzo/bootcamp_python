## Tipagem do exercício da aula 3

### Inserindo loops no código

while True:
    try:
        name: str = input("Type your name: ")
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
        salary: float = float(input("Type your salary: "))

        if salary <= 0:
            print('Type a salary that greater than zero')
        else:
            break
    except ValueError as e:
        print(f'{e} - Type a number, not a empty or word/phrase')

while True:
    try:
        bonus_percentage: float = float(input("Type your bonus percentage: "))

        if bonus_percentage < 0:
            print('Type a non-negative percentage')
        else:
            break
    except ValueError as e:
        print(f'{e} - Type a number, not a empty or word/phrase')

bonus_value: float = 1000 + salary*(bonus_percentage/100)
print(f'💸💸💸   {name} your bonus in this year is .... ${bonus_value}   💸💸💸')