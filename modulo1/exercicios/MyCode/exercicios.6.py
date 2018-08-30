from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_fecundidade="https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

site_connect_municipio = Scrapy_Table(url_municipios)
site_connect_fecundidade = Scrapy_Table(url_fecundidade)

municipios_table = site_connect_municipio.get_tables(0)
fecundidade_table = site_connect_fecundidade.get_tables(1)

print('exercicio 6')

total_populacao = 0

for municipio in municipios_table[1:]:
    total_populacao += float(municipio[4])

print(total_populacao)