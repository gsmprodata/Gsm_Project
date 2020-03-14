from cmp_.db import app, db

class processor_brand(db.Model):
    __tablename__ = 'processor_brand'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean)

class processor(db.Model):
    __tablename__ = 'processor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    processor_brand_id = db.Column(db.Integer, db.ForeignKey("processor_brand.id"), nullable=False)
    is_active = db.Column(db.Boolean)

class storage_type(db.Model):
    __tablename__ = 'storage_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean)
