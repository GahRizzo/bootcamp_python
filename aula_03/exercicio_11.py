### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

word = input('Type a word:')

KEY_WORD = 'roupa'

while word != KEY_WORD:
    word = input('Type the password:')
else:
    print('Congratulation, you have typed the password')
        