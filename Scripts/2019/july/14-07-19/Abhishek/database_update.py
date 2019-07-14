import psycopg2
import sys
import re
#this method will return the display size..................
asciiList = {"zero": 48,"nine":57, "dot":46}
def getDisplaySize(displayString):
    display = ''
    for disChar in displayString:
        if((ord(disChar)>= asciiList["zero"] and ord(disChar) <= asciiList["nine"]) or ord(disChar) == asciiList["dot"]):
            display += disChar
        else:
            break
    return display

#Get resolution details of the model.....
def getResolution(resolutionString):
    resolution = ''
    find_comma =resolutionString.find(',')
    if(find_comma >1 ):
        resolutionArr = re.findall("\d{3,}\sx\s\d{3,}",resolutionString[:find_comma])
        if(len(resolutionArr)>0):
            resolution = resolutionArr[0]
    return resolution

def getHighestData (attrString):
    attr ='0'
    stringToMatch = ['MP', 'mp']
    datArr = attrString.split(',')
    for data in datArr:
        if(stringToMatch[0] in data or stringToMatch[1] in data ):
            number =''
            checkMP = False
            findP = False
            for charData in data:
                if((ord(charData)>= asciiList["zero"] and ord(charData) <= asciiList["nine"]) or ord(charData) == asciiList["dot"]):
                    number += charData
                    checkMP = True
                else:
                    if(checkMP):
                        if(findP):
                            if(charData == 'p' or charData == 'P'):
                                break
                            else:
                                checkMP = False
                                findP = False
                                number = ''

                        if(charData == 'm' or charData == 'M'):
                            findP = True
            if(number != ''):
                if(float(number) > float(attr)):
                    attr = number
    return attr

def getHighestVideoPixel (videoString):
    pixels ='0'
    stringToMatch = ['P', 'p']
    datArr = videoString.split(',')
    for data in datArr:
        if(stringToMatch[0] in data or stringToMatch[1] in data ):
            number =''
            checkP = False
            for charData in data:
                if((ord(charData)>= asciiList["zero"] and ord(charData) <= asciiList["nine"]) or ord(charData) == asciiList["dot"]):
                    number += charData
                    checkP = True
                else:
                    if(checkP):
                        if(charData == 'p' or charData == 'P'):
                            break
                        else:
                            checkP = False
                            number =''
            if(number != ''):
                if(float(number) > float(pixels)):
                    pixels = number
    return pixels


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
        try:
            #don't use [:4] as it will create out of bound index 
            #displaySize = data_list_display['Size'][:4].strip()
            displaySize = ''
            if("Size" in data_list_display):
                if(data_list_display['Size'] != ''):
                    # do the task of fetching display size.
                    displaySize = getDisplaySize(data_list_display['Size'])
            data_dict['display_size'] =displaySize
            #resolution
            resolution = ''
            if("Resolution" in data_list_display):
                if(data_list_display["Resolution"]):
                    resolution = getResolution(data_list_display['Resolution'])
            data_dict['resolution']=resolution
        except(Exception,psycopg2.DatabaseError ) as error:
            print(error)
        #camera
        try: 
            data_list_camera = all_data[7]
            mainCamera = ''
            if "Single" in data_list_camera:
                if(data_list_camera["Single"] != ''):
                    maincamera = getHighestData(data_list_camera["Single"])
            
            elif "Triple" in data_list_camera:
                if(data_list_camera["Triple"] != ''):
                    maincamera = getHighestData(data_list_camera["Triple"])
            elif "Dual" in data_list_camera:
                if(data_list_camera["Dual"] != ''):
                    maincamera = getHighestData(data_list_camera["Dual"])
            else:
                maincamera=""
            data_dict['maincamera'] = maincamera
            #video resolution
            if "Video" in data_list_camera:
                video_resolution = getHighestVideoPixel(data_list_camera['Video'])
            else:
                video_resolution = ""
            data_dict["videoresolution"] = video_resolution
            print(data_dict, all_data[15])
            # print(all_data[0])
        except(Exception,psycopg2.DatabaseError ) as error:
            print(error)
        # print(video_resolution)
        # print(data_dict)
        # sys.exit()
except(Exception,psycopg2.DatabaseError ) as error:
    print(error)
finally:
    if conn is not None:
            conn.close()
            # print('Database connection closed.')
