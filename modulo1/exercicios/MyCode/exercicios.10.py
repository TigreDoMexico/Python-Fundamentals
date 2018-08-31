from  lib.scrapy_table import Scrapy_Table

url_municipios="https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_por_popula%C3%A7%C3%A3o"
url_homicidio="https://pt.wikipedia.org/wiki/Lista_de_cidades_por_taxa_de_homic%C3%ADdios"

site_connect_municipio = Scrapy_Table(url_municipios)
site_connect_homicidio = Scrapy_Table(url_homicidio)

municipios_table = site_connect_municipio.get_tables(0)
homicidio_table = site_connect_homicidio.get_tables(1)

print('exercicio 10')
print("")

lista_de_municipios = {}
contador = 0
numero_de_habitantes = 0

print("cidades:")

for municipio in municipios_table[1:]:
    lista_de_municipios[municipio[2]] = int(municipio[-1])
    
for homicidio in homicidio_table[1:]:
    if contador < 50:
        if homicidio[1] in lista_de_municipios:
            print(contador + 1, homicidio[1], "com", lista_de_municipios[homicidio[1]], "pessoas")
            numero_de_habitantes += lista_de_municipios[homicidio[1]]
            contador += 1

print("Total", numero_de_habitantes)