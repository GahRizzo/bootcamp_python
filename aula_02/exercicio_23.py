## Exercício 23
## Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
## Use try-except para lidar com divisões por zero e entradas não numéricas. 
## Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

OPERATION_LIST = ['*','/','+','-']

first_input_value = input('Type the first value: ')
second_input_value = input('Type the second value: ')
operator = input('Type the operator to calculate: ')

try:
    casting_first_value = float(first_input_value)
    casting_second_value = float(second_input_value)

    if operator not in OPERATION_LIST:
        print("""The operator isn't supported""")

except ValueError as e:
    print(f'{e} - The typed value is not a number')

try:
    if operator == '+':
        result = casting_first_value + casting_second_value
    elif operator == '-':
        result = casting_first_value - casting_second_value
    elif operator == '/':
        result = casting_first_value / casting_second_value
    elif operator == '*':
        result = casting_first_value * casting_second_value
    
    print(f'The operation {casting_first_value:0.1f} {operator} {casting_second_value:0.1f} = {result:0.1f}')

except ZeroDivisionError as e:
    print(f'{e} - It is not possible divide a number per zero')