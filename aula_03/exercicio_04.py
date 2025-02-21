### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# importing libs
import re

# Functions
def is_float(string):
    try:
        cast_string = float(string)
        return True
    except ValueError:
        return False

#Variables
validation_email = False
validation_age = False

# Inputs

while validation_email == False:

    user_email = input('Type your email: ')

    if is_float(user_email) or user_email.isspace():
        print("""It's to necessary type a valid email, not a number or a space""")
        validation_email = False
    elif re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', user_email) is None:
        print("""It's necessary type a email with a "@example.com" """)
        validation_email = False
    else:
        validation_email = True

while validation_age == False:

    try:
        user_age = int(input('Type your age: '))
        if user_age < 0:
            print("Please type a number greater then 0")
            validation_age = False
        elif user_age >= 18 and user_age <=65:
            print('Congratulation!! Your information is valid and you were enrolled')
            exit()
        else:
            print("""Sorry, but you don't have the age to enroll on this site""")
            validation_age = True
        
    except ValueError as e:
        print(f"""It's to necessary type a digit in age, not a text or a float""")
        validation_age = False
    
    

        


