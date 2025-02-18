## Exercício 25: Conversão de Tipo com Validação
## Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
## O programa deve converter a string de entrada em uma lista de números inteiros. 
## Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
## Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
## Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

list_input = input('Type a list of numbers separated by commas:')

str_list = list_input.split(",")
numb_list = []

try:
    for i in str_list:
        numb_list.append(int(i))
    print(f'Congratulation, there is the list of numbers: {numb_list}')
except ValueError as e:
        print(f'{e} - Warning, the list is composed by strings')