import psycopg2
import sys
import re

try :
    conn = psycopg2.connect(host="localhost",database = "gsm_new",user="postgres",password='postgres')
    cur = conn.cursor()
    all_data_query = "select * from public.home_allpro"
    cur.execute(all_data_query)
    alldata = cur.fetchall()
    for all_data in alldata:
        data_dict={}
        # display
        data_list_display = all_data[4]
        displaySize = data_list_display['Size'][:4].strip()
        data_dict['display_size'] =displaySize
       #resolution
        find_comma =data_list_display['Resolution'].find(',')
        resolution = re.findall("\d{3,}\sx\s\d{3,}",data_list_display['Resolution'][:find_comma])
        data_dict['resolution']=resolution[0]
        #camera
        data_list_camera = all_data[7]
        if "Single" in data_list_camera:
            find_comma_camera = data_list_camera['Single'].find(',')
            maincamera = data_list_camera['Single'][:find_comma_camera]

        elif "Triple" in data_list_camera:
            find_comma_camera = data_list_camera['Triple'].find(',')
            maincamera = data_list_camera['Triple'][:find_comma_camera]
        elif "Dual" in data_list_camera:
            find_comma_camera = data_list_camera['Dual'].find(',')
            maincamera = data_list_camera['Dual'][:find_comma_camera]
        else:
            maincamera=""
        data_dict['maincamera'] = maincamera
        #video resolution
        if "Video" in data_list_camera:
            video_resolution = data_list_camera['Video']
        else:
            video_resolution = ""
        print(all_data[0])
        print(video_resolution)
        # print(data_dict)
        # sys.exit()
except(Exception,psycopg2.DatabaseError ) as error:
    print(error)
finally:
    if conn is not None:
            conn.close()
            # print('Database connection closed.')
