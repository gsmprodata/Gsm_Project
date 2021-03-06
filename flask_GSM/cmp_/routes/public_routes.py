from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort, Blueprint
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails, paginate, seperate_brands
import sys, json
from cmp_ import app
from cmp_.db import brand, allpro, top_phones, db
from cmp_.models.processor.model import processor, processor_brand, storage_type
from cmp_.models.user.forms import login_form

def title_function(*string):
    return '| '.join(string)+" | phoneworldz.com"


def get_top_phones():
    phone_list = db.session.query(top_phones).filter(top_phones.is_active == True).limit(10).all()
    list = []
    for phone in phone_list:
        phone_information = {"name" : phone.home_allpro.name, "phone_id":       phone.home_allpro.id, "img_name": phone.home_allpro.img_name, "slug":phone.home_allpro.slug,"brand":phone.home_allpro.brand}
        list.append(phone_information)
    return list

@app.route('/')
def home():
    title = "Mobile Phones | Mobile Prices in India | Online Mobile Shopping | phoneworldz.com"
    nav = db.session.query(brand).all()
    top_phones_json = get_top_phones()
    nav = seperate_brands(nav)
    return render_template('home/index.html',nav=nav, top_phone_json = top_phones_json,title=title,metadata={'title':title})


@app.route('/<string:brand_name>')
def brandinfo(brand_name):
    nav = db.session.query(brand).all()
    pagination = paginate(request ,
                    db.session.query(allpro).filter(allpro.brand==brand_name).filter(allpro.release_date != None)
                    .order_by(allpro.release_date.desc()).order_by(allpro.id))
    
    title = title_function(brand_name)
    nav = seperate_brands(nav)
    return render_template ('brands/allpro.html',nav=nav, pagination = pagination, brand = brand_name,title=title,metadata={'brand':brand_name,'title':title})
    

@app.route('/<string:device_brand>/<string:slug>/<int:pro_id>')
def phone_details(device_brand,slug,pro_id):
    nav = db.session.query(brand).all()
    data = db.session.query(allpro).get_or_404(pro_id)
    jsonData = filterPhoneDetails(data)
    brand_name = jsonData['brand_name']
    phone_name = jsonData['name']
    title = title_function(phone_name,brand_name)
    nav = seperate_brands(nav)
    return render_template("phone_details/detail.html",jsonData=jsonData,nav=nav,title=title,metadata={'brand':brand_name,'phone':phone_name,'title':title})

@app.route('/search_phone',methods=['GET'])
def search_phone():
    query = '%'+str(request.args.get('value'))+'%'
    
    print(query)
    # sys.exit()
    suggestion = db.session.query(allpro).filter(allpro.name.ilike(query)).limit(10).all()
    list = []
    for i in suggestion:
        abc={"name":i.name,"id":i.id}
        list.append(abc)
    return_data = json.dumps(list)
    print(type(return_data))
    return return_data

@app.route('/compare_phone',methods=['GET'])
def compare_phone():
    nav = db.session.query(brand).all()
    phoneOneId = request.args.get('phone1')
    phoneTwoId = request.args.get('phone2')
    dataPhoneOne = filterPhoneDetails(db.session.query(allpro).get_or_404(phoneOneId))
    dataPhoneTwo = filterPhoneDetails(db.session.query(allpro).get_or_404(phoneTwoId))
    nav = seperate_brands(nav)
    jsonData = {}
    jsonData['phones']  = [dataPhoneOne, dataPhoneTwo]
    jsonData['nav'] = nav
    return render_template('phone_details/compare.html', jsonData = jsonData)

