from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'c676dfde280ba245'
login = LoginManager(app)
login.login_view = 'login'

from cmp_.routes import public_routes, admin_routes, filter_routes
from cmp_.bundles import bundle