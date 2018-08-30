from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"

site_connect_municipio = Scrapy_Table(url_municipios)

municipios_table = site_connect_municipio.get_tables(0)

print('exercicio 1')

for municipio in municipios_table[1:]:
    print(municipio[1], municipio[2])
