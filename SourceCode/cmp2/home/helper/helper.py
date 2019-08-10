#filter phone details
def filterPhoneDetails(data):
    img_name = data.img_name
    name = data.name
    screen_size =data.head['display']
    if 'display' in data.head:
        resolution = data.head['resolution']
    else:
        resolution = ""
    if 'main_camera' in data.head:
        main_camera = data.head['main_camera']
    else:
        main_camera = ''
    if 'video_pixel' in data.head:
        video_resolution = data.head['video_pixel']
    else:
        video_resolution = ''
    if 'processor' in data.head:
        processor= data.head['processor']
    else :
        processor=''
    if 'ram' in data.head:
        buffer_ram = data.head['ram']
        if len(buffer_ram)<=2:
            ram = buffer_ram+str('GB')
        else:
            ram = buffer_ram+str('MB')
    else:
        ram = ''
    if 'storage' in data.head:
        storage = data.head['storage']
    else :
        storage = ''
    if 'battery' in data.head:
        battery = data.head['battery']
    else:
        battery=''
    if 'battery_type' in data.head:
        battery_type = data.head['battery_type']
    else:
        battery_type=''
    # end head
    return {'body_misc':data.misc,'body_battery':data.battery,'body_features':data.features,'body_comms':data.comms,'body_sound':data.sound,'body_selfie':data.selfiecamera,'body_maincamera':data.maincamera,'body_memory':data.memory,'body_platform':data.platform,'body_display':data.display,'body_body':data.body,'body_launch':data.launch,'body_network':data.network,'battery_type':battery_type,'battery':battery,'storage':storage,'ram':ram,'processor':processor,'video_resolution':video_resolution,'main_camera':main_camera,'screen_size':screen_size,'img_name':img_name,'name':name,'resolution':resolution}
