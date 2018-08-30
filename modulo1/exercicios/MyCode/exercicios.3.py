from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"

site_connect_municipio = Scrapy_Table(url_municipios)

municipios_table = site_connect_municipio.get_tables(0)

print('exercicio 3')

estados = {}

for municipio in municipios_table[1:]:
    
    estado = municipio[3]
    populacao = int(municipio[4])

    if populacao > 100000:
        if estado in estados:
            estados[estado] += 1
        else:
            estados[estado] = 1

maior_populacao = 0
nome_estado = "NONE"

for est in estados:
    if estados[est] > maior_populacao:
        maior_populacao = estados[est]
        nome_estado = est

print(nome_estado, "possui", maior_populacao, "cidades acima de 100.000 habitantes")