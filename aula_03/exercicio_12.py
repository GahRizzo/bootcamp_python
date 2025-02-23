### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:
    try:
        value = int(input('Type a number between 1 and 10: '))
        if value < 0 or value > 10:
            print('Invalid Value')
            pass
        else:
            print('✔️  Sucess - your number is validated')
            break
    except ValueError or TypeError as e:
        print(f'{e} - You need input a integer number')