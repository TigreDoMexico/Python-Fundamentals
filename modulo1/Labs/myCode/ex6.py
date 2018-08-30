from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

site_connect = Scrapy_Table(url)

tables = site_connect.get_tables(5)

partido_count = {}

for row in tables[1:]:
    votos = int(row[2].replace(".", "").split(" ")[0])
    partido = row[1]

    if partido in partido_count:
        partido_count[partido] += votos
    else:
        partido_count[partido] = votos

for partido in partido_count:
    print(partido, "->", partido_count[partido])