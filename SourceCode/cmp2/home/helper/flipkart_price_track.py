import requests as r
import sys
from bs4 import BeautifulSoup  as b
import lxml.html as l
import json
from .helper import error_msg

def flipkart_data(product_name):
    clean_product_name = str(product_name).replace(' ','')
    url = F'https://www.flipkart.com/search?q={clean_product_name}'

    head = {'Host':'www.flipkart.com','Accept':'*/*'}
    res= r.get(url,headers=head)
    # print(res.content)
    # sys.exit()
    if res.status_code==200:
        string = l.fromstring(res.content)
        doc = string.xpath('//script[@id="jsonLD"]/text()')
        if len(doc) > 0:
            json_data = json.loads(doc[0])
            json_itemlists =  json_data['itemListElement']
            return json_itemlists
        else:
            return error_msg
test_record = flipkart_data('iphone6')
print(test_record[0]['url'])
