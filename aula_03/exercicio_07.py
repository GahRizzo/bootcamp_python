### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

number_list = input("Type a list of numbers, separated by comma: ")

split_list = number_list.replace(" ","").split(',')


casting_list = []
normalized_list = []

for number in split_list:
    cast_number = float(number)
    casting_list.append(cast_number)

for number in casting_list:
    normalized_number = round((number - min(casting_list))/(max(casting_list) - min(casting_list)),2)
    normalized_list.append(normalized_number)

print(f'The normalized numbers for your list is: {normalized_list}')