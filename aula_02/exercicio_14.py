# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

user_date = input("""Type a date with the format "dd/mm/aaaa": """ )

splited_date = user_date.split('/')

print(f'The day of your date is {splited_date[0]}, the month is {splited_date[1]} and the year is {splited_date[2]}')