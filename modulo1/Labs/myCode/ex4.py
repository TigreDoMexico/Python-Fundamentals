from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

site_connect = Scrapy_Table(url)

table = site_connect.get_tables(5)

for row in table[1:]:

    name = row[0]

    first_name = name.split(" ")

    if first_name[0].lower() in ['josé', 'eduardo','joão']:
        print(name)