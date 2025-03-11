# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

word: str = input('Type a word: ')

word_dictionary = {}

for e in word:
    word_dictionary[f"{e.lower()}"] = word_dictionary.get(e.lower(),0) + 1

print(word_dictionary)