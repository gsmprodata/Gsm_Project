from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails
import sys,json
from cmp_.db import brand, allpro, top_phones, db,top_phones
from cmp_ import app
from cmp_.models.user.forms import login_form
from cmp_.routes.public_routes import get_top_phones
import json,datetime
from cmp_.models.user.models import User
from flask_login import current_user,login_user,logout_user,login_required



def get_slider_device():
    phone_list = db.session.query(top_phones).filter(top_phones.is_active == True).all()
    list = []
    for phone in phone_list:
        phone_information = {"name" : phone.home_allpro.name, "phone_id":       phone.home_allpro.id, "img_name": phone.home_allpro.img_name, "slug":phone.home_allpro.slug,"brand":phone.home_allpro.brand}
        list.append(phone_information)
    return list

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
      return redirect(url_for('dashboard'))

    form = login_form()
    if form.validate_on_submit():
      print(form.remember_me.data)
      user = User.query.filter_by(username=form.username.data).first()
      if user is None or not user.check_password(form.password.data):
        flash('Invalid Username or password','danger')
        return redirect(url_for('login'))
      login_user(user,remember=form.remember_me.data)
      return redirect(url_for('dashboard'))
      print('asdsasda')
    return render_template('login.html',form =form)

@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    phone_list = get_slider_device()
    return render_template('admin/slider.html',list=phone_list)

@app.route('/addDevicesToslider',methods=['GET'])
@login_required
def addDevicesToslider():
  device = request.args.get('key')
  list_of_device = json.loads(device)
  flag='False'
  try:
    for i in list_of_device:
      rowCount = db.session.query(top_phones).filter_by(phone_id=int(i)).count()
      if int(rowCount) ==0:
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
  
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))




  

