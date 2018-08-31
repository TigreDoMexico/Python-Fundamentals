from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_homicidio="https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios"
url_fecundidade="https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

site_connect_fecundidade = Scrapy_Table(url_fecundidade)
site_connect_municipio = Scrapy_Table(url_municipios)
site_connect_homicidio = Scrapy_Table(url_homicidio)

municipios_table = site_connect_municipio.get_tables(0)
homicidio_table = site_connect_homicidio.get_tables(1)
fecundidade_table = site_connect_fecundidade.get_tables(1)

print('exercicio 9')
print("")

lista_de_municipios = {}
lista_de_estados = {}
lista_de_fecundidade = {}

for municipio in municipios_table[1:]:
    lista_de_municipios[municipio[2]] = int(municipio[-1])
    lista_de_estados[municipio[2]] = municipio[3]

for fecundidade in fecundidade_table[1:]:
    lista_de_fecundidade[fecundidade[1]] = fecundidade[2]

for homicidio in homicidio_table[1:]:
    if float(homicidio[-1].replace(",",".")) > 60:
        if homicidio[1] in lista_de_municipios:
            print("Cidade:", homicidio[1])
            estado = lista_de_estados[homicidio[1]]
            print("Estado:", lista_de_estados[homicidio[1]])
            print("Populacao:", lista_de_municipios[homicidio[1]])
            print("Taxa de fecundidade:", lista_de_fecundidade[estado])
            print("")
            