### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

value = 999

while value < 0 or value > 10:
    try:
        value = int(input('Type a number between 1 and 10: '))
    except ValueError or TypeError as e:
        print(f'{e} - You need input a integer number')
print('✔️  Sucess - your number is validated')

