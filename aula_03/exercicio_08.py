### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

incompleted_list = {
    'name':'Gabriel Rizzo da Silva'
    ,'age':'30 anos'
    ,'graduated':'s'
    ,'address':None
    ,'number':None
    ,'state':None
}

completed_list = {
    'name':'Gabriel Rizzo da Silva'
    ,'age':'30 anos'
    ,'graduated':'s'
    ,'address':'Rua Lavinia'
    ,'number':1
    ,'state':'SP'
}

list_to_check = incompleted_list
none_list = []

for info in list_to_check:
    if list_to_check.get(info) is None:
        none_list.append(info)
    else:
        next

if len(none_list) == 0:
    print('Success! Your informations have been checked and it is correct')
else:
    print(f'Warning - The following information is empty: {none_list}')    
