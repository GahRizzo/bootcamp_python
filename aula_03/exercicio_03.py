### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.


log_dict = {
    'timestamp': '2021-06-23 10:00:00'
    , 'level': 'ERROR'
    , 'message': 'Falha na conexão'
}

if log_dict.get('level').lower() == 'error':
    print(f'Warning! The read log contain a ERROR registry = {log_dict.get('message')}')
else:
    print("""Passed! The log don't contain errors""")