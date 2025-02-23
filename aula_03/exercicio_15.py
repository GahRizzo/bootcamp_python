### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

list = ['Neque', 'porro', 'quisquam', 'est', 'qui', 'dolorem', 'ipsum']

STOPED_WORD = 'qui'

list_position = 0

while list_position < len(list):
    if list[list_position] == STOPED_WORD:
        print('Your word has been founded')
        break
    list_position += 1
else:
    print("""Sorry, but your word doesn't exist in the list""")