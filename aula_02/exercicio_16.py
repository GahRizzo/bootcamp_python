# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

def cast_bool(input):
    if input == "True":
        return True
    elif input == "False":
        return False
    else:
        print("Invalid")

first_bool = cast_bool(input('Type True or False for the first parameter: ').capitalize())
second_bool = cast_bool(input('Type True or False for the second parameter: ').capitalize())

print(f'The operation AND between the parameters is {first_bool & second_bool}')