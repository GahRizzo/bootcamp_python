# Dada a lista ["maçã", "banana", "cereja"] e o 
# dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

items_list: list = ["maçã", "banana", "cereja"]

items_price: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total_value: int = 0

for e in items_list:
    total_value += items_price.get(e)

print(f'The total cart value is R${total_value:.2f}')