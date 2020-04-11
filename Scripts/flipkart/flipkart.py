import requests as r
import urllib
import sys
from lxml import html
import re 
import sys
import psycopg2
import time
import os

print(os.getcwd())

def name_check(lst,strr):
    flag = True
    for i in lst:
        if i.lower() not in strr.lower():
            flag = False
            return flag
    return flag

def is_exist(tb_name):
    cur.execute(f"SELECT to_regclass('{tb_name}')")
    return bool(cur.fetchall()[0][0])
log_path = os.path.join(str(os.getcwd()),'log.txt')
print(log_path)
with open(log_path,'w') as txtFile:
    conn = psycopg2.connect(user="postgres",
                            password = "Phon*Wor!d@123",
                            host = '51.15.202.105',
                            port = '5432',
                            database ='gsm_dev_test'
                            )
    cur = conn.cursor()

    
    # sys.exit()
    fkp_table = 'public.fkp'

    allProQuery = "select name,brand,id from public.home_allpro where release_year =2018 order by (id)"
    if(is_exist(fkp_table)):
        cur.execute("select dbname from public.fkp  order by(id) desc limit 1")
        lastphone =cur.fetchall()[0][0]
        cur.execute(f"select id from public.home_allpro where  name='{lastphone}'")
        lastPhoneId = cur.fetchall()[0][0]
        print(lastPhoneId)
        allProQuery = f"select name,brand,id from public.home_allpro where release_year =2018 and id>{lastPhoneId} order by (id)"


    txtFile.write("table dropped"+'\n')
    if(not is_exist(fkp_table)):
        cur.execute("create table public.fkp(id serial NOT NULL,dbname varchar(255) ,fk_name varchar(255) ,brand varchar(255) ,ram varchar(255) ,ram_type varchar(255) ,rom varchar(255) ,rom_type varchar(255),price integer,PRIMARY KEY(id))")
        conn.commit()
   

    # sys.exit()
    cur.execute(allProQuery)
    allPro = cur.fetchall()
    for i in allPro:
        print(i)



        db_name = name= i[0]
        if 'watch' in db_name.lower():
            continue
        brand = i[1]
        array_name = name.split(' ')
        url_name = urllib.parse.quote(name)
        url = r'https://www.flipkart.com/search?q='+str(url_name)
        htmlstr = r.get(url)
        tree = html.fromstring(htmlstr.text)
        nameLst = tree.xpath("//div[@class='_3wU53n']/text()")
        feat = tree.xpath("//ul[@class='vFw0gD']/li[1]/text()")
        price = tree.xpath("//div[@class='_1vC4OE _2rQ-NK']/text()")
        if len(nameLst) >0:
            for no in range(len(nameLst)):
                if name_check(array_name,nameLst[no]):
                    fk_name = nameLst[no]
                    try:
                        feat_arr = feat[no].split('|')
                    except:
                        txtFile.write(f"error occured on spliting ({fk_name})"+'\n')
                        continue

                    #ram
                    try:
                        ram_size = re.findall('\d+',feat_arr[0])[0]
                    except:
                        ram_size ='N/A'
                        txtFile.write(f"error occured at ramsize({fk_name})"+'\n')

                    try:
                        ram_type = 'MB'
                        if 'gb' in feat_arr[0].lower():
                            ram_type = 'GB'
                    except:
                        ram_type='N\A'
                        txtFile.write(f"error occured at ram_type({fk_name})"+'\n')

                    #rom
                    try:
                        rom_size = re.findall('\d+',feat_arr[1])[0]
                    except:
                        txtFile.write(f"error occured at rom_size({fk_name})"+'\n')
                        rom = 'N/A'


                    try:
                        rom_type = 'MB'
                        if 'gb' in feat_arr[1].lower():
                            rom_type = 'GB'
                    except:
                        rom_type='N/A'
                        txtFile.write(f"error occured at rom_type({fk_name})"+'\n')

                    try:
                        fk_price_ = re.findall('\d+',price[no])
                        fk_price= int(''.join(fk_price_))
                    except:
                        fk_price='N/A'
                        txtFile.write(f"error occured at price({fk_name})"+'\n')

                    # sys.exit()

                    try:
                        insert = "INSERT INTO public.fkp(dbname, fk_name, brand, ram, ram_type, rom, rom_type, price)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                        data_to_insert = (db_name,fk_name,brand,ram_size,ram_type,rom_size,rom_type,fk_price)
                        cur.execute(insert,data_to_insert)
                        conn.commit()
                    except:
                        txtFile.write(f"error occured at insertion({fk_name})"+'\n')

            time.sleep(2)



                
                # sys.exit()