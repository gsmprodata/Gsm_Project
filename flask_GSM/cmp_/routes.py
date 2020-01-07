from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort
from flask_sqlalchemy import SQLAlchemy
from cmp_.helper.helper import filterPhoneDetails
import sys,json
from cmp_.db import brand,allpro,db
from cmp_ import app





@app.route('/')
def home():
    nav = db.session.query(brand).all()
    return render_template('index.html',nav=nav)


@app.route('/data/<string:brand_name>')
def brandinfo(brand_name):
    print(brand)
    nav = db.session.query(brand).all()
    # data = allpro.objects.filter(brand=brand)
    data = db.session.query(allpro).filter(allpro.brand==brand_name)
    for i in data:
        print(i.img_name)
    # return render(request, 'list.html', {'contacts': contacts})
    return render_template ('allpro.html',data=data,nav=nav)
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
    pass
