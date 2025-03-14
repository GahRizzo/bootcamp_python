### Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

products = [
    {"id": 1, "name": "Headset", "price": 235},
    {"id": 2, "name": "Mouse", "price": 120},
    {"id": 3, "name": "Monitor", "price": 750}
]

for product in products:
    if product['name'] == "Mouse":
        product['price'] = 166

print(f'The updated list is: {products}')