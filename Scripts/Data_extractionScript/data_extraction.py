import requests  as r 
import psycopg2
import lxml.html 
import sys
import json
import urllib.request
import os

	
try:
    conn = psycopg2.connect(host="localhost",database="gsm_new", user="postgres", password="postgres")
    cur = conn.cursor()
    print('connection done')
except:
    print('connection fail')
    sys.exit()

def unique(name):
    name = str(name)
    is_unique = False
    select =  f"SELECT COUNT(*) FROM public.home_allpro WHERE Name = '{name}'"
    try:
        cur.execute(select)
        max_id_val = cur.fetchone()[0]
        if max_id_val <= 0:
            is_unique = True
        print(F'{name} is phone unique =  {is_unique}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return is_unique
    # gets the number of rows affected by the command executed
    row_count = cur.rowcount
    if(row_count == 0):
        val = True
    return val

def extract_head(html):
    try:
        os = html.xpath('//span[@data-spec="os-hl"]/text()')[0].replace("'","")
    except:
        os = ''
    try:   
        ram = html.xpath('//span[@data-spec="ramsize-hl"]/text()')[0].replace("'","")
    except:
        ram = ''
    try:
        body = html.xpath('//span[@data-spec="body-hl"]/text()')[0].replace("'","")
    except:
        body = ''
    try:
        date = html.xpath('//span[@data-spec="released-hl"]/text()')[0].replace("'","")
    except:
        date = ''
    try:
        name = html.xpath("//h1[@class='specs-phone-name-title']/text()")[0].replace("'","")
    except:
        name = ''
    try:
        battery = html.xpath('//span[@data-spec="batsize-hl"]/text()')[0].replace("'","")
    except:
        battery=''
    try:    
        display = html.xpath('//span[@data-spec="displaysize-hl"]/text()')[0].replace("'","")
    except:
        display = ''
    try:    
        storage = html.xpath('//span[@data-spec="storage-hl"]/text()')[0].replace("'","")
    except:
        storage = ''
    try:    
        processor = html.xpath('//div[@data-spec="chipset-hl"]/text()')[0].replace("'","")
    except:
        processor = ''
    try:
        resolution = html.xpath('//div[@data-spec="displayres-hl"]/text()')[0].replace("'","")
    except:
        resolution = ''
    try:    
        main_camera = html.xpath('//span[@data-spec="camerapixels-hl"]/text()')[0].replace("'","")
    except:
        main_camera = ''
    try:
        video_pixel = html.xpath('//div[@data-spec="videopixels-hl"]/text()')[0].replace("'","")
    except:
        video_pixel = ''
    try: 
        battery_type = html.xpath('//div[@data-spec="battype-hl"]/text()')[0].replace("'","")
    except:
        battery_type = ''

    json_ = {
        "os": os,
        "ram": ram,
        "body": body,
        "date": date,
        "name": name,
        "battery":battery,
        "display": display,
        "storage": storage,
        "processor": processor,
        "resolution": resolution,
        "main_camera": main_camera,
        "video_pixel": video_pixel,
        "battery_type": battery_type
    }
    return json.dumps(json_)


def image_download(name,url):
    try:
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)
        dir_path = os.path.dirname(os.path.realpath(__file__))+'/images/'+name
        urllib.request.urlretrieve(url,dir_path)
    except (Exception) as error:
        print (error)


def pagination_links(url):
    res = r.get(url)
    doc = lxml.html.fromstring(res.content)
    list_of_pages = doc.xpath('//div[@class="nav-pages"]/a/@href')
    return list_of_pages


def extract_page(url):#extract page content
    # link1 = "https://www.gsmarena.com/samsung-phones-9.php"
    res = r.get(url)
    doc = lxml.html.fromstring(res.content)
    return doc

def complete_link(url):
    return 'https://www.gsmarena.com/'+url

def get_json_key(html,table_no):
    key_list = []
    class_count = len(phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr/td[@class='ttl']"))
    for i in range(1,class_count+1):
        val = phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr["+str(i)+"]/td[@class='ttl']/a/text()")
        if len(val)==1:
            key_list.append(val[0])
        else:
            key_list.append("")
    return key_list

def get_value(html,table_no):
    value_list = []
    class_count = len(phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr/td[@class='nfo']"))
    for i in range(1,class_count+1):
        val = phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr["+str(i)+"]/td[@class='nfo']/a/text()")
        if len(val)==1:
            value_list.append(val[0])
        else:
            val = phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr["+str(i)+"]/td[@class='nfo']/text()")
            if len(val)==1:
                value_list.append(val[0])
            else:
                value_list.append("")

    key_list = []
    class_count = len(phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr/td[@class='ttl']"))
    for i in range(1,class_count+1):
        val = phone_page_html.xpath("//div[@id='specs-list']/table["+str(table_no)+"]/tr["+str(i)+"]/td[@class='ttl']/a/text()")
        if len(val)==1:
            key_list.append(val[0])
        else:
            key_list.append("")
    return json.dumps(dict(tuple(zip(key_list,value_list))))

def max_id():
    select = f"SELECT max(id) FROM home_allpro"
    max_id_val = 0
    try:
        cur.execute(select)
        max_id_val = cur.fetchone()[0]
        print(F'Finding Max index {max_id_val}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return max_id_val

def unique_urlcheck(name):
    is_unique = True
    select = f"SELECT count(1) FROM home_allpro where upper(name) ='{name}'"
    try:
        cur.execute(select)
        max_id_val = cur.fetchone()[0]
        if max_id_val > 0:
            is_unique = False
        print(F'{name} is phone unique =  {is_unique}')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return is_unique

doc = extract_page('https://www.gsmarena.com')
brand_list = doc.xpath('//div[@class="brandmenu-v2 light l-box clearfix"]/ul/li/a/@href')
brand_names = doc.xpath('//div[@class="brandmenu-v2 light l-box clearfix"]/ul/li/a/text()')
index_val = max_id()+1
skip_check = True
for (brand_link,brand_name) in zip(brand_list,brand_names):
    if(brand_name == 'Sharp'):
        skip_check = False
    if skip_check:
        continue
    pages=[]
    pages.append(brand_link)
    pages.extend(pagination_links(complete_link(brand_link)))
    for page in pages:
        page_html = extract_page(complete_link(page))
        # page_html = extract_page('https://www.gsmarena.com/samsung_galaxy_a70s-9899.php')
        phone_links = page_html.xpath('//div[@class="makers"]/ul/li/a/@href')
        for phone_link in phone_links:
            phone_checkarr = ''
            try:
                phone_checkarr = phone_link.split('-')[0].replace('_',' ').upper().replace("'","")
            except (Exception) as error:
                print(error)
            if(unique_urlcheck(phone_checkarr)):
                # phone_url = complete_link('https://www.gsmarena.com/samsung_galaxy_a70s-9899.php')
                phone_url = complete_link(phone_link)
                phone_page_html = extract_page(phone_url)
                name = ''
                try:
                    name = phone_page_html.xpath("//h1[@class='specs-phone-name-title']/text()")[0].replace("'","")
                except (Exception) as error:
                    print(error)
                if(unique(name)):
                    brand = name.split(' ')[0]
                    head = extract_head(phone_page_html)
                    network = get_value(phone_page_html,1)
                    launch = get_value(phone_page_html,2)
                    body = get_value(phone_page_html,3)
                    display = get_value(phone_page_html,4)
                    platform = get_value(phone_page_html,5)
                    memory = get_value(phone_page_html,6)
                    main_camera = get_value(phone_page_html,7)
                    selfie_camera = get_value(phone_page_html,8)
                    sound = get_value(phone_page_html,9)
                    comms = get_value(phone_page_html,10)
                    feature = get_value(phone_page_html,11)
                    battery = get_value(phone_page_html,12)
                    misc = get_value(phone_page_html,13)
                    # test = get_value(phone_page_html,14)
                    img_url = None
                    img_name = None
                    if len(phone_page_html.xpath("//div[@class='specs-photo-main']/a/img/@src")) >0:
                        img_url = phone_page_html.xpath("//div[@class='specs-photo-main']/a/img/@src")[0]
                        img_name = name.replace(' ','_')+'.jpg'
                        img_name = img_name.replace('/','_')
                        image_download(img_name,img_url)
                    false = False
                    insert = f"INSERT INTO public.home_allpro(id,network, launch, body, display, platform, memory, maincamera, selfiecamera, sound, comms, features, battery, misc, brand, name, img_name, head, flipkart_url, link_tried) VALUES ({index_val},'{network}','{launch}','{body}','{display}','{platform}','{memory}','{main_camera}','{selfie_camera}','{sound}','{comms}','{feature}','{battery}','{misc}','{brand}','{name}','{img_name}','{head}','{''}','{false}')"

                    try:
                        print(F'trying to insert phone name {name}')
                        cur.execute(insert)
                        conn.commit()
                        index_val+=1
                        print('data entered')
                    except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                        





