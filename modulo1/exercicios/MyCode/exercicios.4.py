from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"

site_connect_municipio = Scrapy_Table(url_municipios)

municipios_table = site_connect_municipio.get_tables(0)

print('exercicio 4')

menor = 0
lista = []

for mun in municipios_table[1:]:
    if menor == 0:
        menor = int(mun[-1])
    else:
        if int(mun[-1]) < menor:
            lista = mun

print(lista[2], ",", lista[3], "-", lista[-1], "habitantes")