from  lib.scrapy_table import Scrapy_Table

url_fecundidade="https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

site_connect_fecundidade = Scrapy_Table(url_fecundidade)

fecundidade_table = site_connect_fecundidade.get_tables(1)

print('exercicio 7')

for fecundidade in fecundidade_table[1:]:
    if float(fecundidade[2].replace(",", ".")) > 2.1:
        print(fecundidade[1])