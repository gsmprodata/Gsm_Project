from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails, paginate
import sys, json
from cmp_.db import brand, allpro, top_phones, db
from cmp_.models.processor.model import processor, processor_brand, storage_type
from cmp_.models.user.forms import login_form
from cmp_ import app
from cmp_.routes.url_string import filters

@app.route(f"{filters.controller}{filters.action.getprocessorbrands}", methods=['GET'])
def get_filter_processor_brands(): 
    brand_name = request.args.get('value')

    if not(brand_name == None):
        processors = processor_brand.query.with_entities(processor_brand.id , processor_brand.name).filter(name.ilike(f"%{brand_name}%")).limit(10).all()
    else:
        processors = processor_brand.query.with_entities(processor_brand.id , processor_brand.name).all()
    list = []
    for item in processors:
        processr={"name":item.name,"id":item.id}
        list.append(processr)
    return jsonify(list)

@app.route(f"{filters.controller}{filters.action.getprocessorbybrand}", methods=['GET'])
def get_filter_processor(): 
    brandid = request.args.get('brandid')

    if not(brandid == None):
        processors = processor.query.with_entities(processor.id , processor.name).filter(processor.processor_brand_id==brandid and processor.is_active == true).all()
    else:
        processors = processor.query.with_entities(processor.id , processor.name).limit(10).all()
    list = []
    for item in processors:
        processr={"name":item.name,"id":item.id}
        list.append(processr)
    return jsonify(list)
