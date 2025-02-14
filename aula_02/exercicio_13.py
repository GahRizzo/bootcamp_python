# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

user_phrase = input('Type a phrase here: ')

strip_user_phrase = user_phrase.strip()

print(f'The phrase without spaces is: {strip_user_phrase}')
