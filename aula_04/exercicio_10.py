## Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

number_list = [1,3,4,5,18,22,35,44,62,87,54,43]

odd_list = sorted([number for number in number_list if number%2 == 0])
even_list = sorted([number for number in number_list if number%2 != 0])

print(f'Odd list: {odd_list}')
print(f'Even list: {even_list}')