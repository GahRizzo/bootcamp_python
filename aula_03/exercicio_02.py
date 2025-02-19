### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

try:
    temperature = float(input('Type the temperature: '))
except ValueError as e:
    print(f"""'{e} - String isn't accepted'""")
    exit()

if temperature < 18:
    print('The temperature classification is cold')
elif temperature >= 18 and temperature <= 26:
    print('The temperature classification is normal')
else:
    print('The temperature classification is high')