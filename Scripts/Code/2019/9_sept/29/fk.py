import requests as r
import sys
from bs4 import BeautifulSoup  as b
import lxml.html as l
import json

def fk_data(product_name):
    clean_product_name = str(product_name).replace(' ','')
    url = F'https://www.flipkart.com/search?q={clean_product_name}'

    head = {'Host':'www.flipkart.com','Accept':'*/*'}
    res= r.get(url,headers=head)
    # print(res.content)
    # sys.exit()
    if res.status_code==200:
        string = l.fromstring(res.content)
        doc = string.xpath('//script[@id="jsonLD"]/text()')
        return doc
print(fk_data('iphone6')[0])
