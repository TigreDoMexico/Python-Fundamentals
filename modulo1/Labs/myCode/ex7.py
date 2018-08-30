from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"
url_jato="https://pt.wikipedia.org/wiki/Lista_de_pessoas_envolvidas_na_Opera%C3%A7%C3%A3o_Lava_Jato"

site_connect = Scrapy_Table(url)
site_jato = Scrapy_Table(url_jato)

tables = tuple(site_connect.get_tables(5))
lista_lava_jato = tuple(site_jato.get_tables(1))

lista_investigados = ()

for investigados in lista_lava_jato[1:]:
    lista_investigados = lista_investigados + (investigados[0],)

for vereador in tables[1:]:
    if vereador[0] in lista_investigados:
        print(vereador)

# vereador = "Aécio Neves"
# if vereador in lista_investigados:
#     print(vereador)