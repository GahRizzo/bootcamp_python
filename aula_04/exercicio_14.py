### Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dictionary = {"a": 1, "b": 2, "c": 3}

pair_list = list(dictionary.items())
key_list = list(dictionary.keys())
value_list = list(dictionary.values())

print(f"Pair key and value list: {pair_list}\nKey list: {key_list}\nValue list: {value_list}")