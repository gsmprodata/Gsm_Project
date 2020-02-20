from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails
import sys,json
from cmp_.db import brand, allpro, top_phones, db,top_phones
from cmp_.forms import login_form
from cmp_ import app
from cmp_.forms import login_form
from cmp_.routes import get_top_phones
import json,datetime

def get_slider_device():
    phone_list = db.session.query(top_phones).filter(top_phones.is_active == True).all()
    list = []
    for phone in phone_list:
        phone_information = {"name" : phone.home_allpro.name, "phone_id":       phone.home_allpro.id, "img_name": phone.home_allpro.img_name, "slug":phone.home_allpro.slug,"brand":phone.home_allpro.brand}
        list.append(phone_information)
    return list

@app.route('/login',methods=['GET','POST'])
def login():
    form = login_form()
    return render_template('login.html',form =form)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    phone_list = get_slider_device()
    return render_template('admin/slider.html',list=phone_list)

@app.route('/addDevicesToslider',methods=['GET'])
def addDevicesToslider():
  device = request.args.get('key')
  list_of_device = json.loads(device)
  flag='False'
  try:
    for i in list_of_device:
      db.session.add(top_phones(phone_id=int(i),is_active=True,created_at=datetime.datetime.now()))
      db.session.commit()
      flag = 'True'

    return flag
  except:
    return flag

@app.route('/deleteDeviceFromSlider',methods=['GET','POST'])
def deleteDeviceFromSlider():
  device = request.args.get('id')
  flag = 'False'
  try:
    db.session.query(top_phones).filter_by(phone_id=device).delete()
    db.session.commit()
    flag = 'True'
    return flag

  except:
    return flag
  


  

