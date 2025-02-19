### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

try:
    quantity = float(input('Type the quantity: '))
    price = float(input('Type the price: '))
except ValueError as e:
    print(f"""'{e} - String isn't accepted'""")
    exit()

if quantity > 0 and price > 0:
    print('Congrats! Your data is valid')
else:
    print('Something wrong! The quantity or the price are negative')