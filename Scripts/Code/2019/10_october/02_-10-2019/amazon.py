import psycopg2
import sys
import re
import requests as r
import sys
from bs4 import BeautifulSoup  as b
import lxml.html as l
import json

def mobile(mobile_name_):
    mobile_name = mobile_name_.replace(' ','+')
    url = f'https://www.amazon.in/s?k={mobile_name}&rh=n%3A976419031%2Cn%3A1805560031&dc&qid=1570952238&rnid=3576079031&ref=sr_nr_n_2'
    header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','cookie':'session-id=260-6439958-3988045; ubid-acbin=258-1806248-7821312; amznacsleftnav-abf23d22-2875-4fed-8d82-c9289c2c08fc=1; sst-acbin=Sst1|PQES5TaFswziIw2pzDyR-SbQC8-2AqN2fFAwEHEA1aE3QuDdHDQ5al2pSm9Q1GtA2_T2QlVksEuNZ8T4DYgBrIIAsWDj-apTXZ89rnslUp9JEe2i0DAxHls50Vgw_eFNuV8Zkq2mcXQuAWxm6jYLHa68pndIvDwpRhWP7QUYbXtz_ezCEh80FYATAsYpF469Wdk7Iql5zbihGvQGHtWck-bxvdJOijNMTupl8e_wtcjXk8n61kcAeWd54goVbcUKsKm5dtkuHW5OD0_nWl1Uao23sZDwYclD6tP5Ko47OBZyHmdCGCwPuslxdlGVweYqZj9m1CoCzPLRMUvmNZOlMlAhPQ; i18n-prefs=INR; x-wl-uid=15dHobkk6nExFCodDd52hqPghagRUQcb6weEjQFAQaDAJHqrnxmRr4ewF9gEkmNGdjxqybm3iaVOT0oTcHs2K73Er0hye9cJkti/e0iIkQvAG5bOOj+Tjly/75pdrH6h6qf3rED0HYhM=; amznacsleftnav-4f861904-d765-4e21-9b65-e0c9d5787f18=1; amznacsleftnav-cc35280d-c678-4529-ae2c-c7a10c2cad11=1; session-token=Xj60Jj6il6zl5fvJp4uuvTREso3ibNuBmVno2YMlUtv0/i9Z+kN+h29plnKBU+8ftKFcj1PWnz00oP92CCXuoIr2Oq+AD7NoVdbfNoddEuOTjyB4Xx/DWZU2BUWHtFQlR/jv0MDsArqdcr8EGbP3c499MUME03Du03F0mxeNz4k90ekDfGKKmK4y7ulfAW1p; visitCount=66; session-id-time=2082758401l; csm-hit=tb:91N770YY222PY980J40A+s-5Q3GGVJNC8X9Z8DD9JB9|1570952297349&t:1570952297349&adb:adblk_yes','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    res = r.get(url,headers=header)
    string = l.fromstring(res.content)
    name  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'][1]/a/span/text()")
    doc  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2'][1]/a/@href")
    if mobile_name_.lower() in name[0].lower():
        value = doc[0]
    else:
        value =None
    return value


def watch(watch_name_):
    watch_name = watch_name_.replace(' ','+')
    url = f'https://www.amazon.in/s?k={watch_name}&rh=n%3A5605728031&ref=nb_sb_noss'
    header = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','cookie':'session-id=260-6439958-3988045; ubid-acbin=258-1806248-7821312; amznacsleftnav-abf23d22-2875-4fed-8d82-c9289c2c08fc=1; sst-acbin=Sst1|PQES5TaFswziIw2pzDyR-SbQC8-2AqN2fFAwEHEA1aE3QuDdHDQ5al2pSm9Q1GtA2_T2QlVksEuNZ8T4DYgBrIIAsWDj-apTXZ89rnslUp9JEe2i0DAxHls50Vgw_eFNuV8Zkq2mcXQuAWxm6jYLHa68pndIvDwpRhWP7QUYbXtz_ezCEh80FYATAsYpF469Wdk7Iql5zbihGvQGHtWck-bxvdJOijNMTupl8e_wtcjXk8n61kcAeWd54goVbcUKsKm5dtkuHW5OD0_nWl1Uao23sZDwYclD6tP5Ko47OBZyHmdCGCwPuslxdlGVweYqZj9m1CoCzPLRMUvmNZOlMlAhPQ; i18n-prefs=INR; x-wl-uid=15dHobkk6nExFCodDd52hqPghagRUQcb6weEjQFAQaDAJHqrnxmRr4ewF9gEkmNGdjxqybm3iaVOT0oTcHs2K73Er0hye9cJkti/e0iIkQvAG5bOOj+Tjly/75pdrH6h6qf3rED0HYhM=; amznacsleftnav-4f861904-d765-4e21-9b65-e0c9d5787f18=1; amznacsleftnav-cc35280d-c678-4529-ae2c-c7a10c2cad11=1; session-token=Xj60Jj6il6zl5fvJp4uuvTREso3ibNuBmVno2YMlUtv0/i9Z+kN+h29plnKBU+8ftKFcj1PWnz00oP92CCXuoIr2Oq+AD7NoVdbfNoddEuOTjyB4Xx/DWZU2BUWHtFQlR/jv0MDsArqdcr8EGbP3c499MUME03Du03F0mxeNz4k90ekDfGKKmK4y7ulfAW1p; visitCount=66; session-id-time=2082758401l; csm-hit=tb:91N770YY222PY980J40A+s-5Q3GGVJNC8X9Z8DD9JB9|1570952297349&t:1570952297349&adb:adblk_yes','user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    res = r.get(url,headers=header)
    string = l.fromstring(res.content)
    name  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/a[@class='a-link-normal a-text-normal']/span/text()")
    doc  = string.xpath("//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']/a[@class='a-link-normal a-text-normal']/@href")
    if watch_name_.lower() in name[0].lower():
        value = doc[0]
    else:
        value =None
    return value

print(watch('Apple Watch Series 5'))
