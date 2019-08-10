from django.shortcuts import render,get_object_or_404
from .models import brands
from .models import allpro
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import re
import json
from collections import OrderedDict

#search for phone to be populated
def search_phone(request):
    if request.method =="GET":
        query = request.GET['value']
        suggestion = allpro.objects.filter(name__icontains=query)[:10]
        list = []
        for i in suggestion:
            abc={"name":i.name,"id":i.id}
            list.append(abc)
        return HttpResponse(json.dumps(list),content_type="application/json")
#landing page
def landing(request):
    content =  brands.objects.all()
    return render (request,'home/index.html',{'nav':content})

#Get brand wise phone details
def brandinfo(request,brand):
    content =  brands.objects.all()
    data = allpro.objects.filter(brand=brand)
    paginator = Paginator(data, 20) # Show 25 contacts per page

    page = request.GET.get('page')
    data = paginator.get_page(page)
    # return render(request, 'list.html', {'contacts': contacts})
    return render (request,'home/allpro.html',{'contacts':data,'nav':content})

#Get phone details
def compare_phone(request,phone1,phone2):
    content =  brands.objects.all()
    print(phone1)
    print(phone2)
    return render(request,'home/blank.html', {'nav':content})

def prodetail(request,pro_id):
    content =  brands.objects.all()
    data = get_object_or_404(allpro,id=pro_id)
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

    return render(request,"home/detail.html",{'body_misc':data.misc,'body_battery':data.battery,'body_features':data.features,'body_comms':data.comms,'body_sound':data.sound,'body_selfie':data.selfiecamera,'body_maincamera':data.maincamera,'body_memory':data.memory,'body_platform':data.platform,'body_display':data.display,'body_body':data.body,'body_launch':data.launch,'body_network':data.network,'battery_type':battery_type,'battery':battery,'storage':storage,'ram':ram,'processor':processor,'video_resolution':video_resolution,'main_camera':main_camera,'screen_size':screen_size,'img_name':img_name,'name':name,'resolution':resolution,'nav':content})
