## Exercício 24: Classificador de Números
## Escreva um programa que solicite ao usuário para digitar um número. 
## Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
## Adicionalmente, identifique se o número é "par" ou "ímpar".

input_value = input('Type a value: ')

try:
    casting_input = float(input_value)
except ValueError as e:
    print(f'{e} - The typed value is not a number')

if casting_input > 0:
    text_var = 'positive'
elif casting_input < 0:
    text_var = 'negative'
else:
    text_var = 'zero'

if casting_input % 2 == 0:
    type_var = 'even'
else:
    type_var = 'odd'

print(f'The number typed is {text_var} and {type_var}')