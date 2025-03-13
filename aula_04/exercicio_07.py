# Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

age_list = [10,12,14,16,22,27,35,39,45,58,66,78,95]

majority_age = [age for age in age_list if age >= 18]

print(f'The majority ages are: {majority_age}')


