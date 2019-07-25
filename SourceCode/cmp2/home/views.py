from django.shortcuts import render,get_object_or_404
from .models import brands
from .models import allpro
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import re
import json
def search_phone(request):
    if request.method =="GET":
        query = request.GET['value']
        suggestion = allpro.objects.filter(name__icontains=query)
        list = []
        for i in suggestion:
            abc={"name":i.name,"id":i.id}
            list.append(abc)
        return HttpResponse(json.dumps(list),content_type="application/json")

def landing(request):
    content =  brands.objects.all()
    return render (request,'home/index.html',{'nav':content})
def brandinfo(request,brand):
    content =  brands.objects.all()
    data = allpro.objects.filter(brand=brand)
    paginator = Paginator(data, 20) # Show 25 contacts per page

    page = request.GET.get('page')
    data = paginator.get_page(page)
    # return render(request, 'list.html', {'contacts': contacts})
    return render (request,'home/allpro.html',{'contacts':data,'nav':content})
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
        if len(buffer_ram)<2:
            ram = buffer_ram+str('gb')
        else:
            ram = buffer_ram+str('mb')
    else:
        ram = ''
    if 'storage' in data.head:
        storage = data.head['storage']
    else :
        storage = 'storage'
    if 'battery' in data.head:
        battery = data.head['battery']
    if 'battery_type' in data.head:
        battery_type = data.head['battery_type']
    return render(request,"home/detail.html",{'battery_type':battery_type,'battery':battery,'storage':storage,'ram':ram,'processor':processor,'video_resolution':video_resolution,'main_camera':main_camera,'screen_size':screen_size,'img_name':img_name,'name':name,'resolution':resolution})
