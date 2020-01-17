from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails, paginate
import sys, json
from cmp_.db import brand, allpro, top_phones, db
from cmp_.forms import login_form
from cmp_ import app


def get_top_phones():
    phone_list = db.session.query(top_phones).filter(top_phones.is_active == True).limit(10).all()
    list = []
    for phone in phone_list:
        phone_information = {"name" : phone.home_allpro.name, "phone_id": phone.home_allpro.id, "img_name": phone.home_allpro.img_name}
        list.append(phone_information)
    return list

@app.route('/')
def home():
    nav = db.session.query(brand).all()
    top_phones_json = get_top_phones()
    return render_template('index.html',nav=nav, top_phone_json = top_phones_json)


@app.route('/data/<string:brand_name>')
def brandinfo(brand_name):
    nav = db.session.query(brand).all()
    pagination = paginate(request ,
                    db.session.query(allpro).filter(allpro.brand==brand_name).filter(allpro.release_date != None)
                    .order_by(allpro.id).order_by(allpro.release_date.desc()))
    
    return render_template ('allpro.html',nav=nav, pagination = pagination, brand = brand_name)

@app.route('/prodetail/<int:pro_id>')
def prodetail(pro_id):
    nav = db.session.query(brand).all()
    data = db.session.query(allpro).get_or_404(pro_id)
    jsonData = filterPhoneDetails(data)
    print(jsonData)
    return render_template("detail.html",jsonData=jsonData,nav=nav)

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
    jsonData = {}
    jsonData['phones']  = [dataPhoneOne, dataPhoneTwo]
    jsonData['nav'] = nav
    return render_template('compare.html', jsonData = jsonData)


