## Dada uma lista de emails, remover todos os duplicados.

email_list = [
    'gabriel.rizzo@gmail.com'
    ,'gabriel.rizzo@hotmail.com'
    ,'gabriel.rizzo@whp.com'
    ,'gabriel.rizzo@gmail.com'
]

email_set = set(email_list)

print(f'The email list deduplicated is: {email_set}')