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
    img_name=data.img_name
    d=data.display['Size']
    screen_size =d
    name = data.name
    Resolution =data.display['Resolution']
    return render(request,"home/detail.html",{'screen_size':screen_size,'img_name':img_name,'name':name,'Resolution':Resolution})
