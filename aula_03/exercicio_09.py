### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

number_list = [10,21,27,44,57,89,1726]

even_list = [number for number in number_list if number%2 == 0]

print(f'The even numbers in you list are: {even_list}')