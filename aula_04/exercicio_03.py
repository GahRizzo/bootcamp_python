# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

book: dict = {
    "title":"Alice in Quantumland"
    ,"author":"Robert Gilmore"
    ,"year":"1995"
}

info_list: list = book.items()

for e in info_list:
    print(e)