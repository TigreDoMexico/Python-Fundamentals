from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_fecundidade="https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_taxa_de_fecundidade"

site_connect_municipio = Scrapy_Table(url_municipios)
site_connect_fecundidade = Scrapy_Table(url_fecundidade)

municipios_table = site_connect_municipio.get_tables(0)
fecundidade_table = site_connect_fecundidade.get_tables(1)

print('exercicio 5')
print("")

estado_mais_populoso = municipios_table[1][3]
estado_menos_populoso = municipios_table[-1][3]

menor = 0
maior = 0
maior_municipio = []
menor_municipio = []

for mun in municipios_table[1:]:
    if menor == 0:
        menor = int(mun[-1])
        menor_municipio = mun
        maior = int(mun[-1])
        maior_municipio = mun
    else:
        if int(mun[-1]) < menor:
            menor_municipio = mun
        
        if int(mun[-1]) >= maior:
            maior_municipio = mun

for fecundidade in fecundidade_table[1:]:

    if maior_municipio[3].lower() == fecundidade[1].lower():
        print("Municipio mais populoso")
        print(maior_municipio[2], ",", maior_municipio[3])
        print("Taxa de fecundidade de", maior_municipio[3] ,":",fecundidade[2])
        print("")
    
    if menor_municipio[3].lower() == fecundidade[1].lower():
        print("Municipio menos populoso")
        print(menor_municipio[2], ",", menor_municipio[3])
        print("Taxa de fecundidade de", maior_municipio[3] ,":", fecundidade[2])
        print("")