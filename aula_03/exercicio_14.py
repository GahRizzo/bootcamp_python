### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

SERVICE_LIMIT = 15
CODE_ACCESS = 'XpToyu'
connection_counter = 0

while connection_counter <= SERVICE_LIMIT:
    
    key = str(input('Insert the connection code: '))
    connection_counter += 1

    if key == CODE_ACCESS:
        print('✔️  Connected')
        break
    else:
        print('❌ Denied')
else:
    print('The limit of tries has been exceeded')
