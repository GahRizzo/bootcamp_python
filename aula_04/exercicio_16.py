### Objetico: Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def sum(number_list: list) -> float:
    
    sum = 0
    
    for number in number_list:
        sum = sum + number
    
    return sum

number_list = [10,20,30]

print(f"The sum of all elements in the list is: {sum(number_list)}")