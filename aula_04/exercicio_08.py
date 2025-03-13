# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

people = [
    {"name": "Gabriel", "age": 30},
    {"name": "Carol", "age": 30},
    {"name": "Jorge", "age": 40}
]

people.sort(key=lambda people: people["name"])

print(people)