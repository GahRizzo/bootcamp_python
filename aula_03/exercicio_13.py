### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

actual_page = 1
total_pages = 30

while actual_page <= total_pages:
    print(f'Loading the page {actual_page} of {total_pages}')
    actual_page += 1

print('✔️  Success - All pages have been processed')
