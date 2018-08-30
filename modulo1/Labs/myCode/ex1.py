from  lib.scrapy_table import Scrapy_Table

url="https://pt.wikipedia.org/wiki/C%C3%A2mara_Municipal_de_S%C3%A3o_Paulo"

site_connect = Scrapy_Table(url)

tables = site_connect.get_tables(5)

for row in tables[1:]:
    
    name = row[0]

    #print(name[0:8])
    print(name[:8].replace(' ',''))
    


