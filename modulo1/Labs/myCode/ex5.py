from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

site_connect = Scrapy_Table(url)

table = site_connect.get_tables(5)

partido_count = {}

for row in table[1:]:
    
    partido = row[1]
    
    if partido in partido_count:
        partido_count[partido] += 1
    else:
        partido_count[partido] = 1

num_vereadores = 0
nome_partido = "NO"

for part in partido_count:
    if partido_count[part] >= num_vereadores:
        nome_partido = part
        num_vereadores = partido_count[part]

print(nome_partido, "com", num_vereadores, "vereadores")
    