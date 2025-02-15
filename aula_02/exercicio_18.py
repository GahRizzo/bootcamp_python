# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

def cast_bool(input):
    if input == "True":
        return True
    elif input == "False":
        return False
    else:
        print("Invalid")

user_input = cast_bool(input('Type True or False for the first parameter: ').capitalize())

print(f'The opposite value of {user_input} is {not user_input}')