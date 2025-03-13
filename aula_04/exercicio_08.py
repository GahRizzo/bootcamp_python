# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

people = [
    {"name": "Gabriel", "age": 30},
    {"name": "Carol", "age": 30},
    {"name": "Jorge", "age": 40}
]

# ordering_by_name = [name.get('name') for name in people]

people.sort(key=lambda people: people["name"])

print(people)