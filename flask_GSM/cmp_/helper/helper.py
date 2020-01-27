#filter phone details
import math
error_msg = 'No record found'

def replace_linebreak(value):
    replace_item = {}
    for name, data in value.items():
        replace_item[name] = data.replace('\n', '<br/>')
    value = replace_item
    return value


def filterPhoneDetails(data):
    img_name = data.img_name
    name = data.name
    brand_name = data.brand
    battery_type =""
    battery =""
    storage = ""
    ram =""
    processor =""
    video_resolution =""
    main_camera =""
    screen_size = ""
    resolution = ""
    if data.head is not None:
        if 'display' in data.head:
            screen_size =data.head['display']

        if 'resolution' in data.head:
            resolution = data.head['resolution']

        if 'main_camera' in data.head:
            main_camera = data.head['main_camera']

        if 'video_pixel' in data.head:
            video_resolution = data.head['video_pixel']

        if 'processor' in data.head:
            processor= data.head['processor'] 

        if 'ram' in data.head:
            buffer_ram = data.head['ram']
            ram_arr = buffer_ram.split('/')
            if len(buffer_ram)<=2 or len(ram_arr[0]) <= 2:
                ram = buffer_ram+str('GB')
            else:
                ram = buffer_ram+str('MB')

        if 'storage' in data.head:
            storage = data.head['storage']

        if 'battery' in data.head:
            battery = data.head['battery']

        if 'battery_type' in data.head:
            battery_type = data.head['battery_type']

    # end head
    return {'body_misc':data.misc,'body_battery':data.battery,
    'body_features':data.features,'body_comms':data.comms,
    'body_sound':data.sound,'body_selfie':data.selfiecamera,
    'body_maincamera':replace_linebreak(data.maincamera),'body_memory':data.memory,
    'body_platform':data.platform,'body_display':data.display,
    'body_body':data.body,'body_launch':data.launch,'body_network':data.network,
    'battery_type':battery_type,'battery':battery,'storage':storage,'ram':ram,
    'processor':processor,'video_resolution':video_resolution,'main_camera':main_camera,
    'screen_size':screen_size,'img_name':img_name,'name':name,'brand_name':brand_name,'resolution':resolution}

def paginate(request, query):
    page_number = request.args.get('page')
    size = request.args.get('size')
    is_prev = True
    show_first = False
    show_last = False
    page_range = 7
    page_range_median = int(page_range/2)
    is_next = True
    current_page = 1
    page_size = 20
    count = query.count()
    pages_list = []
    
    if not(page_number == None or size == None): 
        current_page = int(page_number)
        page_size = int(size)

    total_pages =  int(math.ceil(count / int(page_size)))
    ##Check if current page lies in the center or after the center point
    ##if current is 7 and range is 7 then list should be shown as  4-5-6-7-8-9-10
    if current_page > page_range_median:
        ##if current is 7 and total pages are 9 then list should be shown as  3-4-5-6-7-8-9
        if current_page + page_range_median > total_pages:
            if total_pages - (2 * page_range_median) > 0:
                starting_page = total_pages - (2 * page_range_median)
                show_first = True
            else:
                starting_page = 1
            for page in range(starting_page , total_pages+1):
                pages_list.append(page)
        else:
            for page in range(current_page-page_range_median, current_page + page_range_median+1):
                pages_list.append(page)
                show_last = True
                if current_page-page_range_median > 1 :
                    show_first = True

    ## Current is 3 or less than 3 then list should be 1-2-3-4-5-6-7
    elif  (current_page <= page_range_median):
        if total_pages >= page_range:
            ending_page = page_range
            show_last = True
        else: 
            ending_page = total_pages
        for page in range (1, ending_page+1):
            pages_list.append(page)


    data = query.offset((current_page-1)*page_size).limit(page_size).all()
    pagination = {
        'total_pages' :total_pages,
        'total_data' : count,
        'current_page' : current_page,
        'page_size' : page_size,
        'is_prev': is_prev,
        'is_next' : is_next,
        'data' : data,
        'to_count': current_page*page_size,
        'from_count': (current_page*page_size)-page_size+1,
        'page_list' : pages_list,
        'show_first' : show_first,
        'show_last' : show_last
    }
    return pagination
    
