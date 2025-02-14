#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

first_value = float(input('Type the first value: '))
second_value = float(input('Type the second value: '))

average = (first_value + second_value) / 2

print(f'The average between the first and second value is: {average:0.1f}')