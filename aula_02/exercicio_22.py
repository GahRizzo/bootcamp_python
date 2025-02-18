# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações)
# .Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

import re
import unicodedata
import string

def removing_accent(string):
    return ''.join(
        c for c in unicodedata.normalize('NFD', string)
        if unicodedata.category(c) != 'Mn'
    )

user_input = input('Type an word or a phrase and verify if it is a palindrome:')

try:
    casting_input = float(user_input)
    print('The input value is a number, please, enter an word or phrase')
    exit

except:
    word_treated = removing_accent(user_input)
    word_treated = ''.join(c for c in word_treated if c not in string.punctuation)
    word_treated = word_treated.replace(" ", "")
    word_treated = word_treated.lower()

    invert_input = word_treated[::-1]

    if word_treated == invert_input:
        print('Congratulations, the word or phrase is a palindrome')
    else:
        print("""Oh no! the word or phrase isn't a palindrome""")