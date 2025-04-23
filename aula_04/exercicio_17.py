### Objetivo: Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
from math import sqrt

input = int(input("Type a number: "))

def prime_number_check(number: int) -> bool:
    
    divider_list = []

    for divider in range(2, number + 1):
        if number % divider == 0:
            divider_list.append(divider)
    
    if len(divider_list) == 0:
        return False
    elif len(divider_list) == 1:
        return True
    else:
        return False

print(f"Is it prime? {prime_number_check(input)}")