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

    if not(brandid == None) and brandid.strip() != "":
        processors = processor.query.with_entities(processor.id , processor.name).filter(processor.processor_brand_id==brandid).filter(processor.is_active == True).all()
    else:
        processors = processor.query.with_entities(processor.id , processor.name).filter(processor.is_active == True).limit(10).all()
    list = []
    for item in processors:
        processr={"name":item.name,"id":item.id}
        list.append(processr)
    return jsonify(list)

@app.route(f"{filters.controller}{filters.action.getfilterdevice}")
def get_filter_device():
    processorid = request.args.get('processorid')
    pagination = paginate(request ,
                    db.session.query(allpro).filter(allpro.processor_id==processorid).filter(allpro.release_date != None)
                    .order_by(allpro.release_date.desc()).order_by(allpro.id))
    
    return render_template ('filter/allpro.html', pagination = pagination)

@app.route(f"{filters.controller}{filters.action.getmorefilterdevice}")
def get_more_filter_device():
    processorid = request.args.get('processorid')
    pagination = paginate(request ,
                    db.session.query(allpro).filter(allpro.processor_id==processorid).filter(allpro.release_date != None)
                    .order_by(allpro.release_date.desc()).order_by(allpro.id))
    
    return render_template ('filter/more_phones.html', pagination = pagination)

@app.route(f"{filters.controller}{filters.action.getsearchedphonelist}")
def gets_phonelistbyname():
    query = '%'+str(request.args.get('value'))+'%'
    print(query)
    # sys.exit()
    suggestion = db.session.query(allpro).filter(allpro.name.ilike(query)).limit(10).all()
    list = []
    for i in suggestion:
        abc={"value":i.name, "label":i.name, "id":i.id}
        list.append(abc)
    return jsonify(list)