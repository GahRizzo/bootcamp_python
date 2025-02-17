## Exercício 21: Conversor de Temperatura
## Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius 
## e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    celsius_temperature = float(input("Type the celsius temperature that you would like to convert to Fahrenheit: "))
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    print(f'The converted temperature is {fahrenheit_temperature:0.1f}ºF')
except ValueError as e:
    print('===========================================================')
    print(f'Python Error: {e}')
    print("The input value isn't a number, it wasn't possible to convert")
    exit