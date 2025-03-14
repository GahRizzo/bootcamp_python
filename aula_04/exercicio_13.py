### Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

stock = {"Headset": 32, "Mouse": 10, "Monitor": 3, "CPU": 0, "Motherboard": 0}

filtered_stock = { key:value for key, value in stock.items() if stock[key] > 0}

print(filtered_stock)