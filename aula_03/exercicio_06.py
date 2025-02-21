### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

import re

text = input("Type a text here: ")

treated_text = re.sub(r'[,."]', '', text).lower().split(' ')

word_dict = {}

for word in treated_text:
    word_dict.update({word:(treated_text.count(word))})

print("The number of times appear are:")
for word in word_dict:
    print(f"""Word "{word}": {word_dict.get(word)}""")