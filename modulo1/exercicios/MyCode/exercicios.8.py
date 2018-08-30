from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"

site_connect_municipio = Scrapy_Table(url_municipios)

municipios_table = site_connect_municipio.get_tables(0)

print('exercicio 8')

estados = {}

for municipio in municipios_table[1:]:
    
    if municipio[3].lower() in ['são paulo', 'minas gerais', 'rio de janeiro', 'espírito santo']:
        if municipio[3].lower() in estados:
            estados[municipio[3].lower()] += int(municipio[4])
        else:
            estados[municipio[3].lower()] = int(municipio[4])

for estado in estados:
    print(estado, "possui", estados[estado], "habitantes")