from django.shortcuts import render,get_object_or_404
from .models import brands
from .models import allpro
from .helper.helper import filterPhoneDetails
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
    dataPhoneOne = filterPhoneDetails(get_object_or_404(allpro,id=phone1))
    dataPhoneTwo = filterPhoneDetails(get_object_or_404(allpro,id=phone2))
    jsonData = {}
    jsonData['phones']  = [dataPhoneOne, dataPhoneTwo]
    jsonData['nav'] = content
    return render(request,'home/compare.html', jsonData)

def prodetail(request,pro_id):
    content =  brands.objects.all()
    data = get_object_or_404(allpro,id=pro_id)
    jsonData = filterPhoneDetails(data)
    jsonData['nav'] = content
    return render(request,"home/detail.html",jsonData)