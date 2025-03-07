# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

number_list: list = (range(1,11))

for element in number_list:
    print(f'The element value is {element} and this element squared 2 is {element**2}')