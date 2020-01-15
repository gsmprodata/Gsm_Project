from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails
import sys,json
from cmp_.db import brand, allpro, top_phones, db,top_phones
from cmp_.forms import login_form
from cmp_ import app
from cmp_.forms import login_form
from cmp_.routes import get_top_phones

@app.route('/login',methods=['GET','POST'])
def login():
    form = login_form()
    return render_template('login.html',form =form)

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
    phone_list = get_top_phones()
    return render_template('admin/slider.html',list=phone_list)
