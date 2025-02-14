# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius_temperature = float(input("Type the celsius temperature that you would like to convert to Fahrenheit: "))

fahrenheit_temperature = (celsius_temperature * 9/5) + 32

print(f'The converted temperature is {fahrenheit_temperature:0.1f}ºF')