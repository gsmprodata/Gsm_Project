from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from cmp_ import app
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Phon*Wor!d@123@51.15.202.105/gsm_dev_test'
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/gsm_new_test'
db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(db.engine,reflect=True)
brand = Base.classes.home_brands #make id in home_brands primary key 
allpro = Base.classes.home_allpro
top_phones = Base.classes.home_top_phones