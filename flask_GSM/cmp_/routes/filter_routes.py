from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort, Blueprint
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails, paginate
import sys, json
from cmp_.db import brand, allpro, top_phones, db
from cmp_.models.processor.model import processor, processor_brand, storage_type
from cmp_.models.user.forms import login_form
from cmp_ import app
from cmp_.routes.url_string import url

@app.route(f"{url.filters.controller}{url.filters.action.get_processor_brands}", methods=['GET'])
def get_processor_brands():
    brand_name = request.args.get('value')

    if not(brand_name == None):
        processors = processor_brand.query.values('id', 'name').filter(name.ilike(f"%{brand_name}%")).limit(10).all()
    else:
        processors = processor_brand.query.with_entities(processor_brand.id , processor_brand.name).all()
    list = []
    for item in processors:
        processr={"name":item.name,"id":item.id}
        list.append(processr)
    return_data = json.dumps(list)
    print(type(return_data))
    return return_data
