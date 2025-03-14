### Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dictionary_1 = {"a": 1, "b": 2, "c": 6}
dictionary_2 = {"d": 3, "e": 4}

merge_dictionary = dictionary_1 | dictionary_2

print(merge_dictionary)