from flask import Flask, escape, request,render_template,url_for,flash,redirect,request,abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from helper.helper import filterPhoneDetails


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/gsm_new'
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine,reflect=True)
brand = Base.classes.home_brands #make id in home_brands primary key 
allpro = Base.classes.home_allpro


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

if __name__ == '__main__':
	app.run(debug=True)