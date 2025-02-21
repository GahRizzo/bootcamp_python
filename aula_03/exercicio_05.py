### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transaction_info = {
    'valor':12000
    ,'hora':20
}

if transaction_info.get('valor') > 10000 or transaction_info.get('hora') < 9 or transaction_info.get('hora') > 20:
    print('TRANSACTION BLOCKED: this transaction value or the hour have been violated')
else:
    print('TRANSACTION OK')