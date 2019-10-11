import psycopg2
import sys
import re
import requests as r
import sys
from bs4 import BeautifulSoup  as b
import lxml.html as l
import json
#this method will return the display size..................
asciiList = {"zero": 48,"nine":57, "dot":46}

def flipkart_data_mobiles(product_name):
    result = None
    try:
        clean_product_name = str(product_name).replace(' ','')
        url = F'https://www.flipkart.com/mobiles/pr?sid=tyy,4io&q={clean_product_name}'
        head = {'Host':'www.flipkart.com','Accept':'*/*'}
        res= r.get(url,headers=head)
        # print(res.content)
        # sys.exit()
        if res.status_code==200:
            string = l.fromstring(res.content)
            doc = string.xpath('//script[@id="jsonLD"]/text()')
            if len(doc) > 0:
                json_data = json.loads(doc[0])
                result =  json_data['itemListElement']
            else:
                result =  None
    except(Exception) as error:
        print(error)
    finally:
        return result

def flipkart_data_Watches(product_name):
    result = None
    try:
        clean_product_name = str(product_name).replace(' ','')
        url = F'https://www.flipkart.com/wearable-smart-devices/smart-watches/pr?sid=ajy,buh&q={clean_product_name}'
        head = {'Host':'www.flipkart.com','Accept':'*/*'}
        res= r.get(url,headers=head)
        # print(res.content)
        # sys.exit()
        if res.status_code==200:
            string = l.fromstring(res.content)
            doc = string.xpath('//script[@id="jsonLD"]/text()')
            if len(doc) > 0:
                json_data = json.loads(doc[0])
                result =  json_data['itemListElement']
            else:
                result =  None
    except(Exception) as error:
        print(error)
    finally:
        return result

try :
    conn = psycopg2.connect(host="localhost",database = "gsm_new",user="postgres",password='postgres')
    cur = conn.cursor()
    #brand = "'HTC','Oppo', 'vivo', 'Asus', 'BlackBerry', 'OnePlus'"
    all_data_query = """select id, name from public.home_allpro where
    (link_tried is null OR Link_tried = false) AND NAME ILIKE '%WATCH%' ORDER BY Brand"""
    cur.execute(all_data_query)
    phones = cur.fetchall()
    count = 0
    for phoneData in phones:
        count+=1
        print(count)
        checkFlag = False
        name = re.sub(r'\([^)]*\)','',phoneData[1]).strip()
        name_arr = name.split(' ')
        name =  name.replace(" ","%20")
        isPhone = True
        url_string = flipkart_data_Watches(name) #flipkart_data_mobiles(name)
        url = None
        byPassLoop = False
        if url_string is None:
            byPassLoop = True 
        else:
            if len(url_string) < 1:
                byPassLoop = True 
        if byPassLoop == False:
            url = url_string[0]['url']
            for split_name in name_arr:
                if split_name.upper() not in url.upper():
                    checkFlag = True
        if byPassLoop == True or checkFlag == True:
            query = F"UPDATE home_allpro set link_tried = True WHERE id = {phoneData[0]}"
            cur.execute(query)
            conn.commit()
            continue
        if checkFlag ==  False :
            query = F"UPDATE home_allpro set flipkart_url = '{url}',link_tried = True  WHERE id = {phoneData[0]}"
            cur.execute(query)
            conn.commit()
            print('updating url of',phoneData[1], ' URL is ', url, '\n')
    
        
except(Exception,psycopg2.DatabaseError ) as error:
    print(error)
finally:
    if conn is not None:
            conn.close()
            # print('Database connection closed.')
