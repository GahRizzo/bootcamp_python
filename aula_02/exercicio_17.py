#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

def cast_bool(input):
    if input == "True":
        return True
    elif input == "False":
        return False
    else:
        print("Invalid")

first_bool = cast_bool(input('Type True or False for the first parameter: ').capitalize())
second_bool = cast_bool(input('Type True or False for the second parameter: ').capitalize())

print(f'The operation OR between the parameters is {first_bool or second_bool}')