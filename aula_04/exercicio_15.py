### Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

text = input("Type a text: ")

treated_text = text.lower()

caracter_dict = {}

for caracter in treated_text:
    if caracter in caracter_dict:
        caracter_dict[caracter] += 1
    else:
        caracter_dict[caracter] = 1

print(f"The caracter list is: \n {caracter_dict}")

exit()