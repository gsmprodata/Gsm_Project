import psycopg2
import sys
import re
import requests as r
import sys
from bs4 import BeautifulSoup  as b
import lxml.html as l
import json

def match_name(mobile_db_name, mob_amz_name):
    name_matched = True
    name_arr = mobile_db_name.split(' ')
    for split_name in name_arr:
        if split_name not in mob_amz_name.lower():
            name_matched = False
    return name_matched

def mobile(mobile_name_):
    value = None
    try:
        mobile_name = mobile_name_.replace(' ','+')
        url = f'https://www.amazon.in/s?k={mobile_name}&rh=n%3A976419031%2Cn%3A1805560031&dc&qid=1570952238&rnid=3576079031&ref=sr_nr_n_2'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        res = r.get(url,headers=header)
        string = l.fromstring(res.content)
        name  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'][1]/a/span/text()")
        doc  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'][1]/a/@href")
        if len(name) > 0:
            if match_name(mobile_name_.lower(),name[0].lower()):
                value = f'https://www.amazon.in/{doc[0]}'
    except(Exception) as error:
        print(error)
    finally:
        return value


def watch(watch_name_):
    value = None
    try:
        watch_name = watch_name_.replace(' ','+')
        url = f'https://www.amazon.in/s?k={watch_name}&&i=electronics&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389402031%2Cn%3A5605728031&dc&qid=1570974715&rnid=976420031&ref=sr_hi_4'
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        res = r.get(url,headers=header)
        string = l.fromstring(res.content)
        name  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/a[@class='a-link-normal a-text-normal']/span/text()")
        doc  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/a[@class='a-link-normal a-text-normal']/@href")
        if len(name) > 0:
            if match_name(watch_name_.lower(),name[0].lower()):
                value = f'https://www.amazon.in/{doc[0]}'
    except(Exception) as error:
        print(error)
    finally:
        return value
        
try :
    conn = psycopg2.connect(host="localhost",database = "gsm_new",user="postgres",password='postgres')
    cur = conn.cursor()
    #brand = "'HTC','Oppo', 'vivo', 'Asus', 'BlackBerry', 'OnePlus'"
    all_data_query = """select id, name from public.home_allpro where
    (amazon_link_tried is null OR amazon_link_tried = false) ORDER BY Brand"""
    cur.execute(all_data_query)
    phones = cur.fetchall()
    count = 0
    watch_string = "WATCH"
    for phoneData in phones:
        count+=1
        print(count)
        checkFlag = False
        name = re.sub(r'\([^)]*\)','',phoneData[1]).strip()
        isPhone = True
        url_string = None
        if(watch_string in name.upper()):
            url_string = watch(name)
        else:
            url_string = mobile(name)
        url = None
        byPassLoop = False
        if url_string is None:
            byPassLoop = True 
        else:
            if len(url_string) < 1:
                byPassLoop = True 
        if byPassLoop == True:
            # query = F"UPDATE home_allpro set amazon_link_tried = True WHERE id = {phoneData[0]}"
            # cur.execute(query)
            # conn.commit()
            print('no url found',phoneData[1], '\n')
            continue
        if checkFlag ==  False :
            # query = F"UPDATE home_allpro set amazon_url = '{url_string}',amazon_link_tried = True  WHERE id = {phoneData[0]}"
            # cur.execute(query)
            # conn.commit()
            print('updating url of',phoneData[1], ' URL is ', url_string, '\n')
    
        
except(Exception,psycopg2.DatabaseError ) as error:
    print(error)
finally:
    if conn is not None:
            conn.close()
            # print('Database connection closed.')
