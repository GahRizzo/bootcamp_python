# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input('Type the base: '))
exponent = float(input('Type the exponent: '))

power = base ** exponent

print(f'The power operation of {base}^{exponent} is: {power:0.1f}')