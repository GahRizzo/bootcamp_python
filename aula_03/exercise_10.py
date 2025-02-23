### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

input_info = {
    "order_1": {
        'product_id':'lorem'
        ,'category':'motor'
        ,'value':127.99
    },
    "order_2":{
        'product_id':'lorem'
        ,'category':'tires'
        ,'value':328.00
    },
    "order_3":{
        'product_id':'lorem'
        ,'category':'motor'
        ,'value':768.92
    },
    "order_4":{
        'product_id':'lorem'
        ,'category':'oil'
        ,'value':66.5
    },
    "order_5":{
        'product_id':'lorem'
        ,'category':'tires'
        ,'value':299.90
    }
}

category_value ={}

for order in input_info.values():
    for key in order:
        if key == 'category':
            if order.get(key) in category_value:
                category_value[order.get(key)] = category_value.get(order.get(key)) + order.get('value')
            else:
                category_value[order.get(key)] = order.get('value')

print(category_value)