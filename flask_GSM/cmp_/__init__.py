from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from cmp_ import routes,admin_routes
from cmp_.bundles import bundle