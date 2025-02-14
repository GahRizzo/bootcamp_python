# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

from math import pi

circle_radius = float(input('Type the circle radius: '))

circle_area = pi * (circle_radius ** 2)

print(f'The circle area is {circle_area:0.1f}')