### Objetivo: Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.

typed_number_list = [10,20,30]
typed_number = 2

def sum_per_item(number_list: list, number: int) -> dict:
    sum_dict = {}

    for num in number_list:
        sum_dict[num] = num + number

    return sum_dict

print(f"Adding the typed number to each element list, the result is: \n{sum_per_item(typed_number_list, typed_number)}")